# author:xuxk
# contact: 徐小康
# datetime:2021/5/19 16:14
# software: PyCharm

"""
文件说明：
"""
import json
import socket
import struct
import os

def my_send(sk,operate_info):
    b_optinfo = (json.dumps(operate_info)).encode('utf-8')
    num = struct.pack('i', len(b_optinfo))
    sk.send(num)
    sk.send(b_optinfo)

#上传
sk = socket.socket()
sk.connect(('127.0.0.1',9000))

#[登录,注册,退出]

#[上传，下载，退出]
operate_info = {'operate':'upload','user':'luke'}
my_send(sk,operate_info)
file_path = r'G:\kfqpopulation-0.0.1-SNAPSHOT.jar'
file_name = os.path.basename(file_path)
file_size = os.path.getsize(file_path)
print(file_name,file_size)
file_info = {'filename':file_name,'filesize':file_size}
my_send(sk,file_info)

# server端接收 写入
with open(file_path,'rb') as f:
    while file_size:
        content = f.read(1024)
        file_size -= len(content)
        sk.send(content)

print('文件上传完毕')

