import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import numpy as np

class LidarNavigator(Node):
    def __init__(self):
        super().__init__('lidar_navigator')
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10)
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        
        # Defined thresholds for safety (Task 2)
        self.front_threshold = 0.5
        self.side_threshold = 0.3

    def scan_callback(self, msg):
        ranges = np.array(msg.ranges)
        
        # TODO 1: Clean data (remove inf/nan)
        # Turtlebot3 LiDAR returns 'inf' when nothing is in range. We replace it with the max range.
        ranges = np.where(np.isinf(ranges) | np.isnan(ranges), msg.range_max, ranges)
        
        # TODO 2: Define regions
        # LiDAR has 360 degrees. Index 0 is directly in front. 
        # Front is -30 to +30 degrees. Left is 30 to 90. Right is 270 to 330.
        front = np.concatenate((ranges[330:360], ranges[0:30]))
        left = ranges[30:90]
        right = ranges[270:330]
        
        # Compute minimum distance in each region
        front_dist = np.min(front)
        left_dist = np.min(left)
        right_dist = np.min(right)
        
        # Console output for debugging
        self.get_logger().info(f"Front: {front_dist:.2f}m | Left: {left_dist:.2f}m | Right: {right_dist:.2f}m")

        twist = Twist()
        
        # TODO 3: Obstacle logic
        if front_dist < self.front_threshold:
            # obstacle in front - stop linear motion to prevent crash
            twist.linear.x = 0.0 
            
            # TODO 4: Turn direction
            if left_dist > right_dist:
                # left clearer
                twist.angular.z = 0.5
            else:
                # right clearer
                twist.angular.z = -0.5
        else:
            # TODO 5: Forward motion
            twist.linear.x = 0.15
            twist.angular.z = 0.0
            
        self.publisher.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = LidarNavigator()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()