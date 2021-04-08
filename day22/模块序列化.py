# author:xuxk
# contact: 徐小康
# datetime:2021/4/7 8:59
# software: PyCharm

"""
文件说明：
"""
# import json
# stu = {'name':'何轻松','sex':'male',1:('a','b')}
# ret = json.dumps(stu)
# print(stu,type(stu))
# print(ret,type(ret))
#
# d= json.loads(ret)
# print('d->',d,type(d))

import pickle
# stu = {'name':'何轻松','sex':'male',1:('a','b')}
# ret = pickle.dumps(stu)
# print(ret)
# d = pickle.loads(ret)
# print(d,type(d))

class Course():
    def __init__(self,name,price):
        self.name = name
        self.price = price

python = Course('python',29800)
ret = pickle.dumps(python)
print(ret)
p = pickle.loads(ret)
print(p.name,p.price)