import os
import time
from multiprocessing import Process

# def func():
#     for i in range(10):
#         time.sleep(0.5)
#         print('子进程:',os.getpid(),os.getppid())
#
# if __name__ == '__main__':
#     print('主进程',os.getpid(),os.getppid())
#     p = Process(target=func)
#     p.start()
#     for i in range(10):
#         time.sleep(0.3)
#         print('*'*i)

# if __name__ == '__main__':  只是在windows上必须写
# 为什么要写

# 能不能给子进程中传参数
# def func(arg):
#     for i in range(10):
#         time.sleep(0.5)
#         print('子进程%s :'%arg,os.getpid(),os.getppid())
#
# if __name__ == '__main__':
#     print('主进程',os.getpid(),os.getppid())
#     p = Process(target=func,args=(1,))
#     p.start()
#     for i in range(10):
#         time.sleep(0.3)
#         print('*'*i)

# 进程之间数据隔离问题
# count = 100
# def func():
#     global count
#     count -= 1
#     print('子进程 ：',count)
#
# if __name__ == '__main__':
#     print('主进程',os.getpid(),os.getppid())
#     p = Process(target=func)
#     p.start()
#     time.sleep(2)
#     print('主进程 ：',count)

# 启动多个进程
# def func(arg):
#     print('子进程%s :'%arg ,os.getpid(),os.getppid())
#
#
# if __name__ == '__main__':
#     for i in range(10):
#         Process(target=func,args=(i,)).start()

# 子进程和父进程之间的关系
# def func(arg):
#     print('子进程%s :'%arg ,os.getpid(),os.getppid())
#     time.sleep(5)
#     print('子进程end')
#
#
# if __name__ == '__main__':
#     for i in range(10):
#         Process(target=func,args=(i,)).start()
#     print('父进程*******')

# 1.父进程和子进程的启动时异步的
# 父进程只负责通知操作系统启动子进程
# 接下来的工作由操作系统接手 父进程继续执行
# 2.父进程执行完毕之后并不会直接结束程序，
# 而是会等待所有的子进程都执行完毕之后才结束
# 父进程要负责回收子进程的资源


# 多进程 写一个并发的socket tcp server
# 上午的概念
# 4:30 计算器作业











