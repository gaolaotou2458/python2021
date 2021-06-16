# author:xuxk
# contact: 徐小康
# datetime:2021/6/10 13:52
# software: PyCharm

"""
文件说明：两种方式有点类似于java 线程的方式
"""
import os
import time
import random
from multiprocessing import Process
# def func(index):
#     time.sleep(random.randint(1,3))
#     print('第%s个邮件已经发功完毕'%index)
#
# if __name__ == '__main__':
#
#     p = Process(target=func,args=(1,))
#     p.start()
#     p.join() # 阻塞 到p进程执行完毕结束阻塞
#     print('10个邮件发送完毕')

'''print最后一个输出'''
# def func(index):
#     #time.sleep(random.randint(1,3))
#     print('第%s个邮件已经发功完毕'%index)
#
# if __name__ == '__main__':
#     p_lst = []
#     for i in range(10):
#         p = Process(target=func,args=(i,))
#         p.start()
#         p_lst.append(p)
#     for p in p_lst:p.join()
#     print('10个邮件发送完毕') # 阻塞 到p进程执行完毕结束阻塞

'''
开启进程的第二种方式:面向对象
'''
# class MyProcess(Process):
#
#
#     def run(self):
#         print('子进程：', os.getpid(),os.getppid())
#
# if __name__ == '__main__':
#     print('主进程', os.getpid())
#     p = MyProcess()
#     p.start()

# 给子进程传递参数
class MyProcess(Process):

    def __init__(self,arg):
        super().__init__()
        self.arg = arg

    def run(self):
        print('子进程：', os.getpid(),os.getppid(),self.arg)

if __name__ == '__main__':

    p = MyProcess('参数')
    p.start()
    print('主进程', os.getpid())