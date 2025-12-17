#!/usr/bin/env python3

import rclpy # ROS2 Python package
from rclpy.node import Node 
from ackermann_msgs.msg import AckermannDriveStamped

class Talker(Node): # the Node itself
    def __init__(self):
        super().__init__('talker') # initialize ROS internals
        self.declare_parameter('v', 0.0)
        self.declare_parameter('d', 0.0)
        # send AckermannDriveStamped messages on /drive
        self.publisher_ = self.create_publisher(
            AckermannDriveStamped, # message type defined in ackermann_msgs
            'drive', # topic name
            10 # queue size
        )

        self.timer = self.create_timer(0.0, self.publish_drive)

    def publish_drive(self):
        msg = AckermannDriveStamped() # create a new empty message

        v = self.get_parameter('v').value
        d = self.get_parameter('d').value

        msg.drive.speed = v
        msg.drive.steering_angle = d

        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = Talker()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

