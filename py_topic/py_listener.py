import rclpy
from std_msgs.msg import String

def listener_callback(msg):
    # py_chatterトピックから受信したStringメッセージの内容を表示します。
    print(msg.data)

def main(args=None):
    # ROS 2通信を使う前に初期化します。コマンドライン引数もここでROS 2に渡します。
    rclpy.init(args=args)
    # ノードを作成します。ノード名はROS 2上でこのプログラムを識別する名前です。
    node = rclpy.create_node('py_listener')
    # py_chatterトピックをString型で受信するSubscriptionを作成します。
    # メッセージを受信するたびにlistener_callbackが呼び出されます。
    # 最後の10は、受信待ちメッセージを保持するキューの深さです。
    subscription = node.create_subscription(String, 'py_chatter', listener_callback, 10)

    # ノードの処理を継続し、メッセージ受信などのイベントを待ち受けます。
    rclpy.spin(node)
    # spin終了後にノードとROS 2を終了します。
    node.destroy_node()
    rclpy.shutdown()


if __name__=='__main__':
    main()