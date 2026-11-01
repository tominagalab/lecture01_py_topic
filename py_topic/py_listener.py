import rclpy
from std_msgs.msg import String

def listener_callback(msg):
    print(msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = rclpy.create_node('py_listener')
    subscription = node.create_subscription(String, 'py_chatter', listener_callback, 10)

    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__=='__main__':
    main()