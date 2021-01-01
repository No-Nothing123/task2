# ロボットシステム学　課題2
##
# 動作環境
    OS:UBUNTU 20.04
# 内容について
    ROSにあるturtlesimパッケージを使って、動かされて亀の位置を出力します。
# 実行方法
### terminalを開きます。terminal1にします。
    $ roscore  
    #　ROSを起動させます。
### 新しいterminal2を開きます。
    $ rosrun turtlesim turtlesim_node
    # 起動すると、背景が青、真ん中に亀がいるウィンドウが開きます。
### また新しいterminal3を開きます。
    $ rosrun turtlesim turtle_telep_key
    # キーボードにある矢印のキーで亀を操作できます。
    (動かない場合は一回terminal3をクリックすると、亀を操作できるはずです)
#### 最後新しいterminal4を開きます。
    $ rosrun task2 turtle_subscriber
    # 起動すると、亀の位置のx,y軸座標が表示されます。またterminal3に戻って、亀を操作しながら、位置座標も一々表示されます。
