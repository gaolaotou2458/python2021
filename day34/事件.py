# author:xuxk
# contact: 徐小康
# datetime:2021/6/11 14:02
# software: PyCharm

"""
文件说明：事件
Event
阻塞事件：wait()方法
    wait是否阻塞时看event对象内部得一个属性
控制这个属性的只
    set()将这个属性的值改成True
    clear（） 改成False
    is_set() 判断当前属性是否为True
"""
import time
from multiprocessing import Process,Event
import random

# 红绿灯
def traffic_light(e):
    print('\033[31m红灯亮\033[0m')
    while True:
        if e.is_set():
            time.sleep(2)
            print('\033[31m红灯亮\033[0m')
            e.clear()

        else:
            time.sleep(2)
            print('\033[32m绿灯亮\033[0m')
            e.set()


def car(e,i):
    if not e.is_set():
        print('car %s 在等待' % i)
        e.wait()
    print('car %s 通过了'%i)

if __name__ == '__main__':
    event = Event()
    p_light = Process(target=traffic_light,args=(event,))
    p_light.daemon =True
    p_light.start()
    p_lst= []
    for i in range(20):
        time.sleep(random.randrange(0,3,2))
        p_car = Process(target=car,args=(event,i))
        p_car.start()
        p_lst.append(p_car)

    for p in p_lst:p.join()

