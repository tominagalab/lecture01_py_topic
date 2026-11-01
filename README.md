# py_topic

`py_topic`は、ROS 2初心者向けの小規模なトピック通信サンプルパッケージです。文字列メッセージを定期的に送信するノードと、受信して表示するノードを用意しています。

## ノード一覧

| 実行コマンド | ノード名 | 説明 |
| --- | --- | --- |
| `ros2 run py_topic talker` | `py_talker` | 0.1秒ごとに文字列を送信します。 |
| `ros2 run py_topic listener` | `py_listener` | 文字列を受信して端末に表示します。 |

## トピック一覧

| ノード | トピック | 型 | 通信 |
| --- | --- | --- | --- |
| `py_talker` | `py_chatter` | `std_msgs/msg/String` | パブリッシュ |
| `py_listener` | `py_chatter` | `std_msgs/msg/String` | サブスクライブ |

`py_talker`は`Hello world`という文字列を送信し、`py_listener`は受信した文字列を表示します。両ノードのキュー深度は10です。

## 実行方法

以下は、ワークスペースが`~/ros2_ws`にあり、ROS 2がインストール済みである場合の手順です。`<ros2ディストリビューション>`は、利用環境に合わせて`humble`や`jazzy`などに置き換えてください。

### 1. ビルド

```bash
cd ~/ros2_ws
source /opt/ros/<ros2ディストリビューション>/setup.bash
colcon build --packages-select py_topic
source install/setup.bash
```

### 2. ノードの起動

端末を2つ開き、それぞれでROS 2とワークスペースの環境を読み込んでください。

**端末1（受信ノード）**

```bash
cd ~/ros2_ws
source /opt/ros/<ros2ディストリビューション>/setup.bash
source install/setup.bash
ros2 run py_topic listener
```

**端末2（送信ノード）**

```bash
cd ~/ros2_ws
source /opt/ros/<ros2ディストリビューション>/setup.bash
source install/setup.bash
ros2 run py_topic talker
```

受信ノードを起動した端末に、送信された文字列が表示されます。終了するには各端末で`Ctrl+C`を押してください。