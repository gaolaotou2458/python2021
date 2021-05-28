# author:xuxk
# contact: 徐小康
# datetime:2021/5/10 10:31
# software: PyCharm

"""
文件说明：
"""
import socket
sk = socket.socket() # 拿手机
sk.connect(('127.0.0.1',9000))

msg = sk.recv(1024)
print(msg)
sk.send(b'hello1')

sk.close()