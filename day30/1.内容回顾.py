# 网络基础
# 局域网中两台机器的通信原理
    # 交换机
    # ip地址
    # ip地址 -arp协议-> mac地址
    # mac地址 ： 全球唯一
    # arp协议 ： 广播 和 单播
        # 通过ip地址获取mac地址
        # 一台机器A发起一个arp请求（只包含ip地址），发送给交换机
        # 交换机接收到请求，广播这条消息
        # 所有的机器都会接收到这个请求，只有和要寻找ip地址吻合的机器B
        # 才会回应交换机的广播，（带着自己的mac地址）
        # 交换机通过单播的形式将回复的B的mac地址发送给A
    # 判断两台机器是不是在同一个局域网内：
        # 子网掩码
        # A机器的ip地址和A的子网掩码 按位与
        # B机器的ip地址和B的子网掩码 按位与
        # 得到的结果如果一致 那么说明两台机器是在一个网段内的

    # 下面两个ip地址是否在同一个网段
    # 192.168.3.2   255.255.0.0
    # 192.168.4.2   255.255.0.0

    # 下面两个ip地址是否在同一个网段
    # 10.3.2.1  255.0.0.0
    # 10.4.3.2  255.0.0.0

# 局域网之间两台机器的通信原理
    # 交换机 路由器
    # 网关ip ：一个局域网内所有的机器对外通信都通过这个网关IP

# osi7层协议-->osi5层协议
# 应用层
# 传输层
    # 端口 ：找到某一台机器上的具体的网络应用
    # tcp 面向连接 可靠 慢 全双工
        # 三次握手 建立tcp连接的过程
        # 发消息
        # 四次挥手 断开tcp连接的过程
    # udp 无连接 不可靠 快
# 网络层
    # ip
    # ipv4、ipv6协议
    # 127.0.0.1
    # 0.0.0.0
# 数据链路层
    # mac地址
    # arp协议
# 物理层

