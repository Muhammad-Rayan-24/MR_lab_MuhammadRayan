import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry

class OdomSubscriber(Node):
    def __init__(self):
        super().__init__('odom_subscriber')
        # Subscribing to /odom
        self.subscription = self.create_subscription(
            Odometry,
            '/odom',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        # Extracting X and Y coordinates to print cleanly
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        self.get_logger().info(f'Received Odometry -> X: {x:.3f}, Y: {y:.3f}')

def main(args=None):
    rclpy.init(args=args)
    node = OdomSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()