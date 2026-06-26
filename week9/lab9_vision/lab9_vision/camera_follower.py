import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from cv_bridge import CvBridge
import cv2
import numpy as np

# ── States ──────────────────────────────────────────────
SEARCH_RED   = 0   # rotating, looking for red sphere
TRACK_RED    = 1   # aligning + moving toward red sphere
SEARCH_GREEN = 2   # rotating, looking for green cuboid
TRACK_GREEN  = 3   # aligning + moving toward green cuboid
DONE         = 4   # finished — just spin in place forever

class CameraFollower(Node):
    def __init__(self):
        super().__init__('camera_follower')
        self.subscription = self.create_subscription(
            Image, '/camera/image_raw', self.image_callback, 10)
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.bridge = CvBridge()

        # ── Tuned parameters (your working values) ──────
        self.kp               = 0.001
        self.center_threshold = 40
        self.stop_area_red    = 550000   # stop distance for red sphere
        self.stop_area_green  = 550000   # stop distance for green cuboid (tune if needed)

        # ── State machine ────────────────────────────────
        self.state = SEARCH_RED

        self.get_logger().info("Vision Tracking Online. Starting with RED sphere hunt...")

    # ── HSV mask helpers ─────────────────────────────────

    def get_red_mask(self, hsv):
        m1 = cv2.inRange(hsv, np.array([0,   100, 100]), np.array([10,  255, 255]))
        m2 = cv2.inRange(hsv, np.array([160, 100, 100]), np.array([180, 255, 255]))
        return cv2.bitwise_or(m1, m2)

    def get_green_mask(self, hsv):
        return cv2.inRange(hsv, np.array([40, 80, 80]), np.array([85, 255, 255]))

    # ── Centroid from mask ───────────────────────────────

    def get_centroid(self, mask):
        M    = cv2.moments(mask)
        area = M["m00"] / 255.0
        if area > 500:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            return cx, cy, area
        return None, None, 0.0

    # ── Proportional tracking toward a target ────────────

    def track(self, twist, cx, area, image_center, stop_area, label):
        error   = image_center - cx
        raw_turn = float(self.kp * error)
        twist.angular.z = max(-1.5, min(1.5, raw_turn))

        self.get_logger().info(
            f"[{label}] Err={int(error)}  Area={int(area)}",
            throttle_duration_sec=1.0)

        if abs(error) < self.center_threshold:
            if area < stop_area:
                twist.linear.x = 0.15   # aligned and far → drive forward
                return False            # not done yet
            else:
                twist.linear.x  = 0.0
                twist.angular.z = 0.0
                self.get_logger().info(f"[{label}] TARGET REACHED.")
                return True             # reached
        else:
            twist.linear.x = 0.0       # still turning
            return False

    # ── Main callback ────────────────────────────────────

    def image_callback(self, msg):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        except Exception as e:
            self.get_logger().error(f"CV Bridge Error: {e}")
            return

        hsv          = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
        red_mask     = self.get_red_mask(hsv)
        green_mask   = self.get_green_mask(hsv)
        # blue cylinder is intentionally ignored — no mask computed

        height, width, _ = cv_image.shape
        image_center     = width // 2
        twist            = Twist()

        # ── State machine ────────────────────────────────

        if self.state == SEARCH_RED:
            rx, ry, rarea = self.get_centroid(red_mask)
            if rarea > 500:
                self.get_logger().info("RED sphere found — switching to TRACK_RED")
                self.state = TRACK_RED
            else:
                twist.angular.z = 0.3   # slow search spin

        elif self.state == TRACK_RED:
            rx, ry, rarea = self.get_centroid(red_mask)
            if rarea > 500:
                reached = self.track(twist, rx, rarea, image_center,
                                     self.stop_area_red, "RED")
                if reached:
                    cv2.imshow("Red Sphere Mask", red_mask)   # show mask on arrival
                    self.state = SEARCH_GREEN
                    self.get_logger().info("Now hunting GREEN cuboid...")
                else:
                    # draw HUD
                    cv2.circle(cv_image, (rx, ry), 10, (0, 0, 255), -1)
                    cv2.line(cv_image, (image_center, ry), (rx, ry), (255, 0, 0), 2)
            else:
                twist.angular.z = 0.3   # lost it — keep spinning

        elif self.state == SEARCH_GREEN:
            gx, gy, garea = self.get_centroid(green_mask)
            if garea > 500:
                self.get_logger().info("GREEN cuboid found — switching to TRACK_GREEN")
                self.state = TRACK_GREEN
            else:
                twist.angular.z = 0.3   # slow search spin

        elif self.state == TRACK_GREEN:
            gx, gy, garea = self.get_centroid(green_mask)
            if garea > 500:
                reached = self.track(twist, gx, garea, image_center,
                                     self.stop_area_green, "GREEN")
                if reached:
                    cv2.imshow("Green Cuboid Mask", green_mask)  # show mask on arrival
                    self.state = DONE
                    self.get_logger().info("All targets reached! Demo complete.")
                else:
                    cv2.circle(cv_image, (gx, gy), 10, (0, 255, 0), -1)
                    cv2.line(cv_image, (image_center, gy), (gx, gy), (255, 0, 0), 2)
            else:
                twist.angular.z = 0.3

        elif self.state == DONE:
            twist.angular.z = 0.3   # spin forever — demo loop visible in Gazebo

        self.publisher.publish(twist)
        cv2.imshow("Robot Camera View", cv_image)
        cv2.waitKey(1)


def main(args=None):
    rclpy.init(args=args)
    node = CameraFollower()
    rclpy.spin(node)
    node.destroy_node()
    cv2.destroyAllWindows()
    rclpy.shutdown()

if __name__ == '__main__':
    main()