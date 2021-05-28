# author:xuxk
# contact: 徐小康
# datetime:2021/5/18 10:56
# software: PyCharm

"""
文件说明：
"""
import socket
sk = socket.socket()
sk.bind(('127.0.0.1',9000))
sk.listen()

