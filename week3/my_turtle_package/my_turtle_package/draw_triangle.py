import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class TriangleNode(Node):
    def __init__(self):
        super().__init__('draw_triangle')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        # Set a long timer so it has time to finish the shape before restarting
        self.timer = self.create_timer(10.0, self.timer_callback)

    def timer_callback(self):
        msg = Twist()
        # Loop 3 times to draw a triangle
        for _ in range(3): 
            # 1. Move forward
            msg.linear.x = 2.0
            msg.angular.z = 0.0
            self.publisher_.publish(msg)
            time.sleep(2)

            # 2. Turn 120 degrees (2.094 radians)
            msg.linear.x = 0.0
            msg.angular.z = 2.094 
            self.publisher_.publish(msg)
            time.sleep(1)

def main(args=None):
    rclpy.init(args=args)
    triangle_node = TriangleNode()
    rclpy.spin(triangle_node)
    triangle_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()