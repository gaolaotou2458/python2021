# author:xuxk
# contact: 徐小康
# datetime:2021/5/20 14:10
# software: PyCharm

"""
文件说明：
"""
import json
import struct
import os
base_path = r'D:\log'

def upload(conn,usr):
    fileinfo_len = conn.recv(4)
    fileinfo_len = struct.unpack('i',fileinfo_len)[0]
    fileinfo_str = (conn.recv(fileinfo_len)).decode('utf-8')
    fileinfo_dic = json.loads(fileinfo_str)
    file_path = os.path.join(base_path,usr,fileinfo_dic['filename'])
    dir = os.path.join(base_path,usr)
    if os.path.exists(dir) == False: os.makedirs(dir)
    with open(file_path,'wb') as f:
        while fileinfo_dic['filesize']:
            content = conn.recv(1024)
            fileinfo_dic['filesize'] -= len(content)
            f.write(content)
    print('接收完毕')