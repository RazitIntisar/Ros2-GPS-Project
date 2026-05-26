import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class GPSSubscriber(Node):
    def __init__(self):
        super().__init__("gps_subscriber")
        self.sub = self.create_subscription(
            String,
            "gps_data",
            self.callback,
            10
        )

    def callback(self, msg):
        self.get_logger().info(f"Received: {msg.data}")


def main():
    rclpy.init()
    node = GPSSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
