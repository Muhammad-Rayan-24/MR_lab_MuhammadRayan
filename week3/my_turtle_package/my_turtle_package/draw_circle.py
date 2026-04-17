import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class CircleNode(Node):
    def __init__(self):
        super().__init__('draw_circle')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        # Timer fires every 0.1 seconds to keep the turtle moving smoothly
        self.timer = self.create_timer(0.1, self.timer_callback)

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 2.0   # Drive forward
        msg.angular.z = 1.5  # Turn continuously
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    circle_node = CircleNode()
    rclpy.spin(circle_node)
    circle_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()