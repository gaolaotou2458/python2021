import socket

sk = socket.socket()
sk.bind(('127.0.0.1',9090))
sk.listen()

conn,addr = sk.accept()
conn.send(b'hello,')
conn.send(b'world')
conn.close()

sk.close()


# 合包现象
    # 数据很短
    # 时间间隔短
# 拆包现象
    # 大数据会发生拆分
    # 不会一次性的全部发送到对方
    # 对方在接受的时候很可能没有办法一次性接收到所有的信息
    # 那么没有接受完的信息很可能和后面的信息黏在一起
# 粘包现象只发生在tcp协议
    # tcp协议的传输 是 流式传输
    # 每一条信息与信息之间是没有边界的

# udp协议中是不会发生粘包现象的
    # 适合短数据的发送
    # 不建议你发送过长的数据
    # 会增大你数据丢失的几率

# 在程序中会出现粘包：收发数据的边界不清晰
# 接收数据这一端不知道要接收数据的长度到底是多少












