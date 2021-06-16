# author:xuxk
# contact: 徐小康
# datetime:2021/6/11 13:54
# software: PyCharm

"""
文件说明：
"""
'''
4个屋子
10个人
'''
from multiprocessing import Process,Semaphore
import time
import random

def ktv(person,sem):
    sem.acquire()
    print('%s走进KTV'%person)
    time.sleep(random.randint(1,5))
    print('%s走出KTV'%person)
    sem.release()

if __name__ == '__main__':
    # 保证进去4个
    sem = Semaphore(4)
    for i in range(10):
        p = Process(target=ktv,args=('person%s'%(i+1),sem))
        p.start()

'''
信号量实现机制
    计数器+锁 实现
'''