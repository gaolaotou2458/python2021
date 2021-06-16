# author:xuxk
# contact: 徐小康
# datetime:2021/6/10 14:59
# software: PyCharm

"""
文件说明：守护进程
"""
from multiprocessing import Process
import time

# def func():
#     print('子进程 start')
#     time.sleep(3)
#     print('子进程 end')
#
# if __name__ == '__main__':
#     p = Process(target=func)
#     ## 主进程结束，子进程也结束，所以是守护进程
#     p.daemon = True
#     p.start()
#     time.sleep(2)
#     print('主进程')

def func1():
    count = 1
    while True:
        time.sleep(0.5)
        print(count*'*')
        count += 1

def func2():
    print('func2 start')
    time.sleep(5)
    print('func2 end')

if __name__ == '__main__':
    p1 = Process(target=func1)
    p1.daemon = True
    p1.start()
    Process(target=func2).start()
    time.sleep(3)
    print('主进程结束')

'''
主进程执行完毕，但是子进程没结束，守护进程是否还执行？
回答：守护进程不会执行，所以执行3s左右
守护进程会跟随主进程代码执行完毕而结束

结论：
主进程会等待子进程结束，守护进程只等待主进程代码结束就结束了

应用： 程序的报活
'''