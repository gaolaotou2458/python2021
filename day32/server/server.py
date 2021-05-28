# author:xuxk
# contact: 徐小康
# datetime:2021/5/19 16:08
# software: PyCharm

"""
文件说明：
"""
import json
import struct
import socketserver
import operate_handler
class MyFTP(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        length = conn.recv(4)
        length = struct.unpack('i',length)[0]
        operate = (conn.recv(length)).decode('utf-8')
        operate_dic = json.loads(operate)
        print(operate_dic['operate'],operate_dic['user'])
        opt = operate_dic['operate']
        getattr(operate_handler,opt)(conn,operate_dic['user'])

socketserver.TCPServer.allow_reuse_address =True #防止端口被占用
server = socketserver.ThreadingTCPServer(('127.0.0.1',9000),MyFTP)
server.serve_forever()


