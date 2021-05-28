# author:xuxk
# contact: 徐小康
# datetime:2021/5/17 14:21
# software: PyCharm

"""
文件说明：
"""
import socket

sk = socket.socket()
sk.bind(('127.0.0.1',9000))

sk.setblocking(False) #非阻塞

sk.listen()
while True:
    try:
        conn,addr = sk.accept()  # 如果没有老链接我，我不在这里等待
    except BlockingIOError:
        conn.recv()  #也不阻塞了