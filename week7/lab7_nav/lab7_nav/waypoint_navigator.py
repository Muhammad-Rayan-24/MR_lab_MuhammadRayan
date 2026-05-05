import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from nav2_msgs.action import FollowWaypoints
from geometry_msgs.msg import PoseStamped
import sys

class WaypointNavigator(Node):
    def __init__(self):
        super().__init__('waypoint_navigator')
        self._client = ActionClient(self, FollowWaypoints, 'follow_waypoints')

    def send_waypoints(self, waypoints):
        self.get_logger().info('Waiting for FollowWaypoints action server...')
        self._client.wait_for_server()
        
        goal_msg = FollowWaypoints.Goal()
        goal_msg.poses = waypoints
        
        self.get_logger().info(f'Sending {len(waypoints)} waypoints...')
        send_goal_future = self._client.send_goal_async(goal_msg)
        rclpy.spin_until_future_complete(self, send_goal_future)
        
        goal_handle = send_goal_future.result()
        if not goal_handle.accepted:
            self.get_logger().error('Goal rejected by server!')
            return
            
        self.get_logger().info('Goal accepted. Navigating...')
        result_future = goal_handle.get_result_async()
        rclpy.spin_until_future_complete(self, result_future)
        self.get_logger().info('All waypoints reached successfully!')

def make_pose(x, y, yaw_w):
    pose = PoseStamped()
    pose.header.frame_id = 'map'
    pose.pose.position.x = float(x)
    pose.pose.position.y = float(y)
    pose.pose.position.z = 0.0
    pose.pose.orientation.z = 0.0
    pose.pose.orientation.w = float(yaw_w)
    return pose

def main(args=None):
    rclpy.init(args=args)
    navigator = WaypointNavigator()
    
    waypoints = []
    
    # Task 3: Dynamic Command Line Arguments
    # Example: ros2 run lab7_nav waypoint_navigator 1.0 1.0 1.0 0.5 0.5 1.0
    if len(sys.argv) > 1:
        args_list = sys.argv[1:]
        if len(args_list) % 3 != 0:
            navigator.get_logger().error("Arguments must be in sets of 3 (X, Y, Yaw_W)")
            return
            
        for i in range(0, len(args_list), 3):
            wp = make_pose(args_list[i], args_list[i+1], args_list[i+2])
            waypoints.append(wp)
        navigator.get_logger().info(f"Loaded {len(waypoints)} dynamic waypoints.")
        
    else:
        # Task 2: Default 5-Waypoint Mission (Tight Safe Box)
        navigator.get_logger().info("No arguments provided. Running default 5-waypoint mission.")
        waypoints = [
            make_pose(0.5, -0.5, 1.0),   # Waypoint 1
            make_pose(-0.5, -0.5, 1.0),  # Waypoint 2
            make_pose(-0.5, 0.5, 1.0),   # Waypoint 3
            make_pose(0.5, 0.5, 1.0),    # Waypoint 4
            make_pose(0.0, 0.0, 1.0),    # Waypoint 5
        ]

    if waypoints:
        navigator.send_waypoints(waypoints)
        
    navigator.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()