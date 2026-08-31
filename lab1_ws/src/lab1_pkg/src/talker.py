#!/usr/bin/env python3

import rclpy
from  rclpy.node import Node
from ackermann_msgs.msg import AckermannDriveStamped

class Talker(Node):
    def __init__(self):
        super().__init__('talker')

        self.declare_parameter('v', 0.0)
        self.declare_parameter('d', 0.0)

        self.v = self.get_parameter('v').value
        self.d = self.get_parameter('d').value

        self.publisher = self.create_publisher(AckermannDriveStamped, 'drive', 10)

    def publish_drive_msg(self):
        msg = AckermannDriveStamped()

        msg.drive.speed = self.v
        msg.drive.steering_angle = self.d

        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = Talker()

    while rclpy.ok():
        node.publish_drive_msg()

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()








