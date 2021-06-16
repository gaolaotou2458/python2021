# author:xuxk
# contact: 徐小康
# datetime:2021/6/11 13:07
# software: PyCharm

"""
文件说明： 锁
抢票
"""
import json
import time
from multiprocessing import Process,Lock

def search(person,lock):
    lock.acquire() #上锁
    with open('ticket') as f:
        dic = json.load(f)
    time.sleep(0.2)
    if dic['count'] > 0:
        print('%s买到了'%person)
        dic['count'] -= 1
        time.sleep(0.2)
        with open('ticket','w') as f:
            json.dump(dic,f)
    else:
        print('%s没买到了' % person)
    lock.release() #释放
if __name__ == '__main__':
    lock = Lock()
    for i in range(10):
        p = Process(target=search,args=('person%s'%i,lock))
        p.start()

# 为了保证数据的安全
# 异步情况下，多个进程有可能同时修改一份资源
# 这时就给修改过程上锁

