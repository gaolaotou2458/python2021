# author:xuxk
# contact: 徐小康
# datetime:2021/6/16 13:33
# software: PyCharm

"""
文件说明：
"""
from multiprocessing import Queue,Process
import queue
# 先进先出
# q = Queue(2)
# q.put(1)
# q.put(2)
#q.put_nowait(3)

# print(q.get())
# print(q.get())
# print(q.get())
# try:
#     print(q.get_nowait())
# except queue.Empty:
#     print('empty')

# print(q.empty())
# print(q.full())
# print(not q.full())

def consume(q):
    print('son-->',q.get())
    q.put({'222': 222})


if __name__ == '__main__':
    q= Queue()
    p = Process(target=consume,args=(q,))
    p.start()
    print(1111)
    q.put({'111': 111})
    p.join()
    print('Foo->',q.get())