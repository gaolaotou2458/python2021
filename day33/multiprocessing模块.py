# author:xuxk
# contact: 徐小康
# datetime:2021/6/7 11:16
# software: PyCharm

"""
文件说明：
"""
# 同步

#异步

#阻塞

#非阻塞

# 同步阻塞
# 异步非阻塞
# IO多路复用
import os
import time
#
# print(os.getpid())  # process
# # time.sleep(200)
# print(os.getppid()) # parent process

from multiprocessing import Process
# def func():
#     for i in range(10):
#         time.sleep(0.5)
#         print('子进程:' os.getpid(),os.getppid())
#
#
# if __name__ == '__main__':
#     print('主进程',os.getpid(),os.getppid())
#     p = Process(target=func)
#     p.start()
#     for i in range(10):
#         time.sleep(0.3)
#         print(i)

## if __name__ == '__main__':
## 为什么要写
'''
只有windows需要写
和子进程创建机制有关
'''


## 能不能给子进程传递参数
# def func(arg):
#     for i in range(10):
#         time.sleep(0.5)
#         print('子进程%s:' %arg,os.getpid(),os.getppid())
#
#
# if __name__ == '__main__':
#     print('主进程',os.getpid(),os.getppid())
#     p = Process(target=func,args=(1,))
#     p.start()
#     for i in range(10):
#         time.sleep(0.3)
#         print(i)
'''

'''
## 进程之间数据隔离问题
# count = 100
# def func():
#     global count
#     count -= 1
#     print('子进程',count)
#
# if __name__ == '__main__':
#     print('主进程',os.getpid(),os.getppid())
#     p = Process(target=func)
#     p.start()
#     time.sleep(0.5)
#     print('主进程',count)


## 启动多个进程
def func(arg):
    print('子进程%s:'%arg,os.getpid(),os.getppid())

if __name__ == '__main__':
    for i in range(10):
        Process(target=func,args=(i,)).start()