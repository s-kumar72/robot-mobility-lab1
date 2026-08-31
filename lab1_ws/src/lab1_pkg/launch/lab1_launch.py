from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='lab1_pkg',
            executable='talker.py',
            name='talker',
            output='screen',
            parameters=[
                {'v': 2.0},
                {'d': 0.5}
            ]
        ),
        Node(
            package='lab1_pkg',
            executable='relay.py',
            name='relay',
            output='screen'
        )
    ])