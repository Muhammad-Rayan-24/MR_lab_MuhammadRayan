import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

class GoToGoalNode(Node):
    # We upgraded the __init__ to accept target_x and target_y from the user!
    def __init__(self, target_x, target_y):
        super().__init__('go_to_goal')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.subscriber_ = self.create_subscription(Pose, 'turtle1/pose', self.update_pose, 10)
        
        self.pose = Pose()
        
        # Set the goals to the user's input
        self.goal_x = target_x 
        self.goal_y = target_y
        self.distance_tolerance = 0.1 
        
        self.timer = self.create_timer(0.1, self.move_turtle)

    def update_pose(self, data):
        self.pose = data

    def move_turtle(self):
        msg = Twist()
        
        distance_error = math.sqrt((self.goal_x - self.pose.x)**2 + (self.goal_y - self.pose.y)**2)
        angle_to_goal = math.atan2(self.goal_y - self.pose.y, self.goal_x - self.pose.x)
        heading_error = angle_to_goal - self.pose.theta
        heading_error = math.atan2(math.sin(heading_error), math.cos(heading_error))

        if distance_error >= self.distance_tolerance:
            msg.linear.x = 1.0 * distance_error
            msg.angular.z = 4.0 * heading_error
            self.publisher_.publish(msg)
        else:
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            self.publisher_.publish(msg)
            self.get_logger().info(f'Goal Reached at X: {self.goal_x}, Y: {self.goal_y}!')
            self.timer.cancel() 

def main(args=None):
    rclpy.init(args=args)
    
    # --- GET USER INPUT BEFORE STARTING THE NODE ---
    print("\n--- Turtlebot Target Controller ---")
    print("The Turtlesim grid is 11.0 x 11.0")
    
    try:
        user_x = float(input("Enter target X coordinate: "))
        user_y = float(input("Enter target Y coordinate: "))
    except ValueError:
        print("Invalid input! Please enter numbers (e.g., 8.5).")
        return

    # Pass the user's input into the node
    go_to_goal_node = GoToGoalNode(user_x, user_y)
    
    print(f"\nDriving to ({user_x}, {user_y})...")
    rclpy.spin(go_to_goal_node)
    
    go_to_goal_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()