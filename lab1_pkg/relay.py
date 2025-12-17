#!/usr/bin/env python3

import rclpy
from rclpy.node import Node 
from ackermann_msgs.msg import AckermannDriveStamped

class Relay(Node):
    def __init__(self):
        super().__init__('relay')

        self.publisher_ = self.create_publisher(
            AckermannDriveStamped, 
            'drive_relay', 
            10
        )

        self.subscriber_ = self.create_subscription(
            AckermannDriveStamped, 
            'drive', 
            self.callback,
            10
        )

    def callback(self, msg):
        speed = msg.drive.speed
        angle = msg.drive.steering_angle

        new_msg = AckermannDriveStamped()
        new_msg.drive.speed = speed * 3
        new_msg.drive.steering_angle = angle * 3

        self.publisher_.publish(new_msg)

def main(args=None):
    rclpy.init(args=args)
    node = Relay()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

