# author:xuxk
# contact: 徐小康
# datetime:2021/5/17 14:39
# software: PyCharm

"""
文件说明：
"""

import hmac
import hashlib
import socket

key = b'alex_s'
sk = socket.socket()
sk.connect(('127.0.0.1',9000))

msg = sk.recv(32)
result = hmac.new(key,msg,hashlib.sha256)
print(result.hexdigest())
res = result.hexdigest()
res = res.encode('utf-8')
sk.send(res)

sk.send(b'upload')


