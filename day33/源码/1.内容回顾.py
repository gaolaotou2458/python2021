# 网络相关的知识
# B/S C/S架构
# ipv4、ipv6
# osi七层协议
    # A机器上发出的二进制信息是按照一个约定的位置和位数来排列的
    # B机器也按照相同的位置和位数来解析这个信息
# osi五层协议
    # 应用层 http/ftp/https/smtp
    # 传输层 端口、tcp/udp协议  四层交换机、四层路由器
    # 网络层 ipv4/ipv6协议      三层交换机、路由器
    # 数据链路层 mac/arp协议    网卡、交换机
    # 物理层
# tcp协议/udp协议
    # tcp 协议的特点 对可靠性要求高的长数据
        # 面向连接的 可靠的 慢的 流式传输
        # 三次握手
        # 四次挥手
        # 粘包问题
            # 拆包机制 nagel算法
            # 合包机制
    # udp协议特点  高并发的短消息
        # 面向数据包的 无连接不可靠的 快速的 短数据传输
        # 不能发送过大的数据
# arp协议
# 根据ip地址找mac地址 —— 交换机 （广播、单播）

# 子网掩码、网段、网关ip

# socket

# socketserver
# 实现了并发的tcp协议的socket的server端
# import socketserver
# class Myserver(socketserver.BaseRequestHandler):
#     def handle(self):
#         conn = self.request
#
# server = socketserver.ThreadingTCPServer((addr),Myserver)
# server.serve_forever()