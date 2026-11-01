import rclpy
from std_msgs.msg import String

def main(args=None):
    rclpy.init(args=args)
    node = rclpy.create_node('py_talker')
    publisher = node.create_publisher(String, 'py_chatter', 10)
    msg = String()
    i = 0

    def timer_callback():
        nonlocal i
        msg.data = "Hello world"
        i+=1
        print('Publishing:', msg.data, i)
        publisher.publish(msg)

    timer_period = 0.1
    timer = node.create_timer(timer_period, timer_callback)
    rclpy.spin(node)
    node.destroy_timer(timer)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()