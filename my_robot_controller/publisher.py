import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random


class GPSPublisher(Node):
    def __init__(self):
        super().__init__("gps_publisher")
        self.pub = self.create_publisher(String, "gps_data", 10)
        self.timer = self.create_timer(1.0, self.send_data)

    def send_data(self):
        lat = 43.65 + random.uniform(-0.01, 0.01)
        lon = -79.38 + random.uniform(-0.01, 0.01)

        msg = String()
        msg.data = f"GPS: {lat:.5f}, {lon:.5f}"

        self.pub.publish(msg)
        self.get_logger().info(msg.data)


def main():
    rclpy.init()
    node = GPSPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
