# author:xuxk
# contact: 徐小康
# datetime:2021/5/18 11:05
# software: PyCharm

"""
文件说明：
"""
import socketserver
# tcp协议的server不需要导入socket
class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        while True:
            conn.send(b'hello')
            print(conn.recv(1024))
        print(self.request)



server = socketserver.ThreadingTCPServer(('127.0.0.1',9000),Myserver)
server.serve_forever()