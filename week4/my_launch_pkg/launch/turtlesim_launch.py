from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        # 1. Start the main simulator window (this automatically creates turtle1)
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim'
        ),
        
        # 2. Automatically call the spawn service to create turtle2
        ExecuteProcess(
            cmd=[
                'ros2', 'service', 'call', '/spawn', 
                'turtlesim/srv/Spawn', 
                "{x: 2.0, y: 2.0, theta: 0.0, name: 'turtle2'}"
            ],
            output='screen'
        )
    ])