import rclpy
from std_msgs.msg import String

def main(args=None):
    # ROS 2通信を使う前に初期化します。コマンドライン引数もここでROS 2に渡します。
    rclpy.init(args=args)
    # ノードを作成します。ノード名はROS 2上でこのプログラムを識別する名前です。
    node = rclpy.create_node('py_talker')
    # String型のメッセージをpy_chatterトピックに送るPublisherを作成します。
    # 最後の10は、送信待ちメッセージを保持するキューの深さです。
    publisher = node.create_publisher(String, 'py_chatter', 10)
    # 送信するStringメッセージを用意します。
    msg = String()
    i = 0

    def timer_callback():
        nonlocal i
        # タイマーから定期的に呼び出され、メッセージを作成して送信します。
        msg.data = "Hello world"
        i+=1
        print('Publishing:', msg.data, i)
        publisher.publish(msg)

    # 0.1秒ごとにコールバックを呼び出すタイマーを作成します。
    timer_period = 0.1
    timer = node.create_timer(timer_period, timer_callback)
    # ノードの処理を継続し、タイマーなどのイベントを待ち受けます。
    rclpy.spin(node)
    # spin終了後にタイマー、ノード、ROS 2を順に終了します。
    node.destroy_timer(timer)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()