import rclpy
from rclpy.node import Node

class ParameterNode(Node):
    def __init__(self):
        super().__init__('parameter_node')
        
        # Declare the parameter with a default empty string
        self.declare_parameter('student_name', 'Muhammad Rayan')
        
        # Retrieve the current value of the parameter
        student_name_param = self.get_parameter('student_name').get_parameter_value().string_value
        
        # Prompt the user for input in the terminal
        user_response = input("This node contains the value of the parameter [student_name]. Do you want to know its value? [y/n]: ")
        
        # Execute logic based on the input
        if user_response.lower() == 'y':
            # Expected behavior from Task 3
            if student_name_param == '':
                self.get_logger().info('student_name not set')
            else:
                self.get_logger().info(student_name_param)
                
        elif user_response.lower() == 'n':
            self.get_logger().info('Understood. Keeping the parameter hidden.')
            
        else:
            self.get_logger().warn('Invalid input detected. Shutting down.')

def main(args=None):
    rclpy.init(args=args)
    node = ParameterNode()
    rclpy.spin_once(node, timeout_sec=0.1)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
