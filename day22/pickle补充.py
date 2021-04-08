# author:xuxk
# contact: 徐小康
# datetime:2021/4/7 14:19
# software: PyCharm

"""
文件说明：
"""
import pickle
class Course():
    def __init__(self,name,price):
        self.name = name
        self.price = price

# python = Course('python',29800)
# with open('pickle_file','wb') as f:
#     pickle.dump(python,f)

'''这里如果注释掉Course类，就报错，因为内存中不存在这个类，读不到'''
# with open('pickle_file','rb') as f:
#     course = pickle.load(f)
# print(course)

python = Course('python',29800)
java = Course('java',29800)
linux = Course('linux',29800)

def my_dump(course):
    with open('pickle','ab') as f:
        pickle.dump(course,f)

# my_dump(python)
# my_dump(java)
# my_dump(linux)

with open('pickle','rb') as f:
    while True:
        try:
            content = pickle.load(f)
            print(content.name)
        except EOFError:
            break



