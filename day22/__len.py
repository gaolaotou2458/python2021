# author:xuxk
# contact: 徐小康
# datetime:2021/4/6 14:44
# software: PyCharm

"""
文件说明：
"""
'''
list
dict
set
tuple
int
float
'''

# print('__len__' in dir(list))
# class Foo:
#     def __len__(self):
#         return 1
#
# obj = Foo()
# print(len(obj))

class Class:
    def __init__(self,name,course):
        self.name = name
        self.course= course
        self.students = []
    def __len__(self):
        return len(self.students)

s1 = Class('骑士1班','python')
s1.students.append('张三')
s1.students.append('杨幂')
s1.students.append('热巴')
print(len(s1))
