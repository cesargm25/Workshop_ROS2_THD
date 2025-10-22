import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MinimalSubscriber2(Node):

    def __init__(self):
        super().__init__('node_subscriber')
        self.subscription = self.create_subscription(
            String,
            'My_second_topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        self.publisher= self.create_publisher(String, 'My_third_topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'hookup again: %d' % self.i
        self.publisher.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1

    def listener_callback(self, msg):
        self.get_logger().info('this is what i get: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber2 = MinimalSubscriber2()

    rclpy.spin(minimal_subscriber2)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber2.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
