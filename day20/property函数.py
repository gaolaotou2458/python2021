# author:xuxk
# contact: 徐小康
# datetime:2021/3/30 8:20
# software: PyCharm

"""
文件说明：
"""
class Student:
    def __init__(self,name):
        self.__name = name

    @property
    def name(self):
        return self.__name + '1111'

    @name.setter
    def name(self,new):
        if type(new) is str:
            self.__name = new

    @name.deleter
    def name(self):
        print('执行我了')
        del self.__name

    @name.getter
    def name(self):
        return self.__name + '2222'

stu = Student("老王")
print(stu.name)
stu.name = '隔壁老王'
print(stu.name)
del stu.name
print(stu.__dict__)
'''
    只有当被property装饰的方法
    又实现了一个同名方法
    且被setter装饰器装饰了
    且在对被装饰的方法赋值的时候 就出发被setter装饰器装饰的方法
'''