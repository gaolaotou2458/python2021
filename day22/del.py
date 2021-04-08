# author:xuxk
# contact: 徐小康
# datetime:2021/4/6 14:10
# software: PyCharm

"""
文件说明：
"""
## 单例模式
class Foo:
    def __init__(self,name,age):
        self.name = name
        self.age =age
        self.file = open('file',mode='w',encoding='utf-8')

    def write(self):
        self.file.write('2112121221')

    def __del__(self):
        # 做一些清理工作，归还操作系统资源
        # 网络操作，IO操作
        self.file.close()
        print('执行了删除')

f = Foo('alex',20)
f.write()
del f



