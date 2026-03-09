import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class RobotMonitor(Node):

    def __init__(self):
        super().__init__('robot_monitor')

        #  para guardar  ultimos valores
        self.velocity = None
        self.battery = None

        # Sub vel
        self.vel_subscription = self.create_subscription(
            Float32,
            '/robot_velocity',
            self.velocity_callback,
            10)

        # sub bat
        self.bat_subscription = self.create_subscription(
            Float32,
            '/robot_battery',
            self.battery_callback,
            10)

    def velocity_callback(self, msg):
        self.velocity = msg.data
        self.evaluate_status()

    def battery_callback(self, msg):
        self.battery = msg.data
        self.evaluate_status()

    def evaluate_status(self):

        if self.velocity is not None:

            if self.velocity > 2.0:
                self.get_logger().info(f'Velocity: {self.velocity:.2f} → WARNING')
            else:
                self.get_logger().info(f'Velocity: {self.velocity:.2f}')

        if self.battery is not None:

            if self.battery < 10:
                self.get_logger().info(f'Battery: {self.battery:.2f} → CRITICAL BATTERY')

            elif self.battery < 20:
                self.get_logger().info(f'Battery: {self.battery:.2f} → LOW BATTERY')

            else:
                self.get_logger().info(f'Battery: {self.battery:.2f}')


def main(args=None):
    rclpy.init(args=args)

    node = RobotMonitor()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()


'''
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32  


class Mysubscriber(Node):

    def __init__(self):
        super().__init__('mi_subscriptor')

        self.subscription = self.create_subscription(
            Int32,           
            'ignaciop',
            self.listener_callback,
            10)

        self.subscription

    def listener_callback(self, msg):
        self.get_logger().info(f'Me llegó este número primo: {msg.data}')


def main(args=None):
    rclpy.init(args=args)

    nodo = Mysubscriber()

    rclpy.spin(nodo)

    nodo.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
'''