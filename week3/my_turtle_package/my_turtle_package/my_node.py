import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class VelocityPublisher(Node):
    def __init__(self):
        super().__init__('velocity_publisher')
        # Create a publisher that talks to the turtle
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Twist()
        # Loop 4 times to draw a square
        for _ in range(4): 
            # 1. Move forward
            msg.linear.x = 2.0
            msg.angular.z = 0.0
            self.publisher_.publish(msg)
            time.sleep(2)

            # 2. Turn 90 degrees (1.57 radians)
            msg.linear.x = 0.0
            msg.angular.z = 1.57 
            self.publisher_.publish(msg)
            time.sleep(1)

def main(args=None):
    rclpy.init(args=args)
    velocity_publisher = VelocityPublisher()
    
    # Keep the node alive
    rclpy.spin(velocity_publisher)
    
    # Cleanup
    velocity_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()