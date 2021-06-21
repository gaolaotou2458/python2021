# author:xuxk
# contact: 徐小康
# datetime:2021/6/17 13:32
# software: PyCharm

"""
文件说明：
"""
from multiprocessing import Pipe,Process

# left, right = Pipe()
# left.send('123')
# print(right.recv())

# def consumer(left,right):
#     left.close()
#     msg = right.recv()
#     print(msg)
#
# if __name__ == '__main__':
#     left,right = Pipe()
#     Process(target=consumer,args=(left,right)).start()
#     left.send(123)

def consumer(left,right):
    left.close()
    while True:
        try:
            print(right.recv())
        except EOFError:
            break

if __name__ == '__main__':
    left, right = Pipe()
    p = Process(target=consumer,args=(left,right))
    p.start()
    right.close()
    for i in range(10):
        left.send('泔水%s'%i)
    left.close()

