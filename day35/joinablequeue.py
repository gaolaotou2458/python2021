# author:xuxk
# contact: 徐小康
# datetime:2021/6/16 15:49
# software: PyCharm

"""
文件说明：
JoinableQueue 类
put
get
 #task_done 通知队列已经有一个数据被处理了
q.join() 阻塞直到放入队列中所有的数据都被处理掉（有多少个数据就接受到多少个taskdone）
"""
from multiprocessing import JoinableQueue,Process

import time
import random
import queue

def consumer(q,name):
    #所有处理数据的内容
    while True:
        food = q.get()
        print('%s吃了一个%s' %(name,food))
        time.sleep(random.uniform(0.5,1)) #模拟吃的时间
        q.task_done()


def producer(q,name,food):
    #获取数据
    for i in range(10):
        time.sleep(random.uniform(0.3,0.8))
        print('%s生产了%s%s' %(name,food,i))
        q.put(food+str(i))


if __name__ == '__main__':
    q = JoinableQueue()
    c1 = Process(target=consumer,args=(q,'alex'))
    c2 = Process(target=consumer, args=(q, 'pig'))
    c1.daemon = True
    c2.daemon = True
    c1.start()
    c2.start()

    p1 = Process(target=producer,args=(q,'老马','蛋糕'))
    p2 = Process(target=producer, args=(q, '老吴', '骨头'))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    q.join()
