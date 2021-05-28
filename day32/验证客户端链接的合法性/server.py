# author:xuxk
# contact: 徐小康
# datetime:2021/5/17 14:39
# software: PyCharm

"""
文件说明：
"""
import socket
import os
import hmac
import hashlib

def auth(conn):
    msg = os.urandom(32)
    conn.send(msg)
    # 处理这个随机字符串，得到一个结果
    result = hmac.new(secret_key, msg, hashlib.sha256)

    print(result.hexdigest())
    # 接收clietn端处理的结果
    client_digest = conn.recv(1024)

    # 对比成功可以继续通信
    if result.hexdigest() == client_digest.decode('utf-8'):
        return True
    else:
        return False

sk = socket.socket()
sk.bind(('127.0.0.1',9000))
sk.listen()



secret_key = b'alex_sb'
conn,addr = sk.accept()

# 生成一个随机的字符串
# 发送到client
if auth(conn):
    print(conn.recv(1024))
else:
    conn.close() # 不成功 close
sk.close()


