import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class Subs(Node):
    def __init__(self):
        super().__init__('ros2_package_subs')
        self.subscription = self.create_subscription(
            Float64,
            'at_fund/sensor',
            self.listener_callback,
            1)
        self.subscription
    def listener_callback(self, msg):
        result = "\nSensor = {0}\n".format(msg)
        self.get_logger().info(result)
        
def main(args=None):
    rclpy.init(args=args)
    subs = Subs()
    rclpy.spin(subs)
    subs.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
