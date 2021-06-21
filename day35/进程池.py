# author:xuxk
# contact: 徐小康
# datetime:2021/6/17 14:22
# software: PyCharm

"""
文件说明：计算型  充分占用CPU
"""
# from multiprocessing import Pool,Process
# import time
#
# def func(num):
#     print('做了第%s件衣服'%num)
#
# if __name__ == '__main__':
#     start = time.time()
#     p = Pool(4)
#     for i in range(500):
#         p.apply_async(func,args=(i,))
#     p.close() #关闭进程池，用户不能再向这个池提交任务了
#     p.join()
#     print(time.time() - start)
#     p_lst = []
#     start = time.time()
#     for i in range(100):
#         p = Process(target=func,args=(i,))
#         p.start()
#         p_lst.append(p)
#     for p in p_lst:p.join()
#     print(time.time() - start)

import time
import os
from multiprocessing import  Pool

def task(num):
    time.sleep(1)
    print('%s : %s' %(num,os.getpid()))
    return num**2

# if __name__ == '__main__':
#     p = Pool(4)
#     for i in range(20):
#         res = p.apply(task,args=(i,)) # 提交任务的方法，同步提交
#         print(res)

if __name__ == '__main__':
    p = Pool()
    for i in range(20):
        res = p.apply_async(task,args=(i,)) # 提交任务的方法，异步提交
        print(res)
    p.close()
    p.join()


