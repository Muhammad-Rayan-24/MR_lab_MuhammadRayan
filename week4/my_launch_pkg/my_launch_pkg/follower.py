import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

class FollowerNode(Node):
    def __init__(self):
        super().__init__('follower_node')
        # We publish velocity commands to turtle2
        self.publisher_ = self.create_publisher(Twist, 'turtle2/cmd_vel', 10)
        
        # We subscribe to BOTH turtles to know exactly where they are
        self.sub_turtle1 = self.create_subscription(Pose, 'turtle1/pose', self.update_pose1, 10)
        self.sub_turtle2 = self.create_subscription(Pose, 'turtle2/pose', self.update_pose2, 10)

        self.pose1 = Pose()
        self.pose2 = Pose()

        # Update the math 10 times a second
        self.timer = self.create_timer(0.1, self.follow_logic)

    def update_pose1(self, data):
        self.pose1 = data

    def update_pose2(self, data):
        self.pose2 = data

    def follow_logic(self):
        # Don't do math if we haven't received coordinates from the simulator yet
        if self.pose1.x == 0.0 or self.pose2.x == 0.0:
            return

        msg = Twist()
        
        # Calculate distance and angle between turtle2 and turtle1
        distance = math.sqrt((self.pose1.x - self.pose2.x)**2 + (self.pose1.y - self.pose2.y)**2)
        angle_to_target = math.atan2(self.pose1.y - self.pose2.y, self.pose1.x - self.pose2.x)

        heading_error = angle_to_target - self.pose2.theta
        heading_error = math.atan2(math.sin(heading_error), math.cos(heading_error))

        # Drive towards turtle1, but stop if we get closer than 0.5 units to avoid a crash!
        if distance > 0.5:
            msg.linear.x = 1.5 * distance
            msg.angular.z = 4.0 * heading_error
        else:
            msg.linear.x = 0.0
            msg.angular.z = 0.0

        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    follower_node = FollowerNode()
    rclpy.spin(follower_node)
    follower_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()