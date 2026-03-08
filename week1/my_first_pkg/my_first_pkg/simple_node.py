import rclpy
from rclpy.node import Node
import os

class SimpleNode(Node):
    def __init__(self):
        super().__init__('simple_node')
        
        # 1. Define the absolute path to our counter file
        file_path = os.path.expanduser('~/Rayan_ros2_ws/src/my_first_pkg/my_first_pkg/counter.txt')
        
        # 2. Read the current count (default to 0 if the file doesn't exist yet)
        count = 0
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                try:
                    count = int(file.read().strip())
                except ValueError:
                    count = 0 # Failsafe if the file is empty or corrupted
                    
        # 3. Increment the counter
        count += 1
        
        # 4. Print the required log message
        self.get_logger().info(f'Welcome to Mobile Robotics lab Muhammad Rayan -- Run count: {count}')
        
        # 5. Save the new count back to the file for the next run
        with open(file_path, 'w') as file:
            file.write(str(count))

def main(args=None):
    rclpy.init(args=args)
    node = SimpleNode()
    # spin_once lets us create the node, log once, and exit cleanly
    rclpy.spin_once(node, timeout_sec=0.1)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

