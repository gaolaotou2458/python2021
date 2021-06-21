# author:xuxk
# contact: 徐小康
# datetime:2021/6/16 14:35
# software: PyCharm

"""
文件说明：
"""
## 消费者
from multiprocessing import Process,Queue
import time
import random
import queue

def consumer(q,name):
    #所有处理数据的内容
    while True:
        food = q.get()
        if food is None:break
        print('%s吃了一个%s' %(name,food))
        time.sleep(random.uniform(0.5,1)) #模拟吃的时间


def producer(q,name,food):
    #获取数据
    for i in range(10):
        time.sleep(random.uniform(0.3,0.8))
        print('%s生产了%s%s' %(name,food,i))
        q.put(food+str(i))

if __name__ == '__main__':
    q = Queue()
    c1 = Process(target=consumer,args=(q,'alex'))
    c2 = Process(target=consumer, args=(q, 'pig'))
    c1.start()
    c2.start()

    p1 = Process(target=producer,args=(q,'老马','蛋糕'))
    p2 = Process(target=producer, args=(q, '老吴', '骨头'))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    q.put(None) #有几个消费者放就给None
    q.put(None)