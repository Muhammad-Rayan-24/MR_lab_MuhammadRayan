import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class VelPublisher(Node):
    def __init__(self):
        super().__init__('vel_publisher')
        # Publishing to /cmd_vel
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        # Timer calls the callback every 2.0 seconds
        self.timer = self.create_timer(2.0, self.timer_callback)
        self.is_moving = False

    def timer_callback(self):
        msg = Twist()
        if self.is_moving:
            msg.linear.x = 0.0
            self.get_logger().info('Publishing: Stop (0.0 m/s)')
        else:
            msg.linear.x = 0.2
            self.get_logger().info('Publishing: Forward (0.2 m/s)')
        
        # Toggle the state
        self.is_moving = not self.is_moving
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = VelPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()