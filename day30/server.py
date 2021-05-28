# author:xuxk
# contact: 徐小康
# datetime:2021/5/10 10:31
# software: PyCharm

"""
文件说明：
"""

import socket
sk = socket.socket() #买手机
sk.bind(('127.0.0.1',9000))  #给手机换一张卡
sk.listen()  #开机
while True:
    conn,addr = sk.accept()  #等电话
    print(conn,addr)
    conn.send(b'hello')
    msg= conn.recv(1024)
    print(msg.decode('utf-8'))

sk.close() #关机
