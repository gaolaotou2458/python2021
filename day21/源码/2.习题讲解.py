# -*- coding: utf-8 -*-
# @Time    : 2018/8/31 9:06
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 2.习题讲解.py
# @Software: PyCharm

'''1. 类变量和实力变量的区别？'''
'''
类：静态变量
实例变量：对象属性
'''
'''
2.super的作用?
在子类中调用父类的方法
'''

'''3.不全代码
    def func(arg):
        判断arg是否可以被调用，如果可以则执行并打印返回结果，否则直接打印结果
'''


# def func(arg):
#     if callable(arg):
#         ret = arg()
#         print(ret)
#     else:
#         print('else' , arg)
#
# class Foo:pass
#
# func(Foo)
# obj = Foo()
# func(obj)

'''
5 补全代码
def func(*arg):
    计算args中函数、方法、Foo类的对象的个数，并返回给调用者
'''
# def func1():pass
# def func2():pass
# class Foo:
#     def method1(self): pass
#     def method2(self): pass
#     def method3(self): pass
# obj = Foo()
# # print(isinstance(obj,Foo))
# from types import MethodType,FunctionType
# def func(*arg):
#     ret = {'函数':0,"方法":0,"Foo类实例":0}
#     for i in arg:
#         if isinstance(i,FunctionType): ret['函数']+=1
#         elif isinstance(i,Foo):ret['Foo类实例']+=1
#         elif isinstance(i,MethodType) : ret['方法']+=1
#     return ret
#
# print(func(obj,func1,func2,obj.method1,obj.method2,obj.method3,Foo(),Foo()))

'''
6 看代码写结果并画图表示对象和类的关系以及执行流程
class StrakConfig(object):
    list_display = []

    def get_list_display(self):
        self.list_display.insert(0, 33)
        return self.list_display

class RoleConfig(StrakConfig):
    list_display = [11,22]

s1 = StrakConfig()
s2 = StrakConfig()

result1 = s1.get_list_display()
print(result1)
result2 = s2.get_list_display()
print(result2)
'''
# class StrakConfig(object):
#     list_display = []
#
#     def get_list_display(self):
#         self.list_display.insert(0, 33)
#         return self.list_display
#
# class RoleConfig(StrakConfig):
#     list_display = [11,22]
#
# s1 = StrakConfig()
# s2 = StrakConfig()
#
# result1 = s1.get_list_display()
# print(result1)
# result2 = s2.get_list_display()
# print(result2)

'''
7 看代码写结果并画图表示对象和类的关系以及执行流程
class StrakConfig(object):
    list_display = []

    def get_list_display(self):
        self.list_display.insert(0, 33)
        return self.list_display

class RoleConfig(StrakConfig):
    list_display = [11,22]

s1 = StrakConfig()
s2 = RoleConfig()

result1 = s1.get_list_display()
print(result1)
result2 = s2.get_list_display()
print(result2)

'''

'''
8 看代码写结果并画图表示对象和类的关系以及执行流程
class StrakConfig(object):
    list_display = []

    def get_list_display(self):
        self.list_display.insert(0, 33)
        return self.list_display

class RoleConfig(StrakConfig):
    list_display = [11,22]

s1 = RoleConfig()
s2 = RoleConfig()

result1 = s1.get_list_display()
print(result1)
result2 = s2.get_list_display()
print(result2)

'''
class StrakConfig(object):
    list_display = []

    def get_list_display(self):
        self.list_display.insert(0, 33)
        return self.list_display

class RoleConfig(StrakConfig):
    list_display = [11,22]

s1 = RoleConfig()
s2 = RoleConfig()

result1 = s1.get_list_display()
print(result1)
result2 = s2.get_list_display()
print(result2)