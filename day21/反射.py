# author:xuxk
# contact: 徐小康
# datetime:2021/3/31 8:16
# software: PyCharm

"""
文件说明：反射
"""
'''
# 反射
# 3w 1h
# what 是什么
    # 反射 使用字符串数据类型的变量名来获取这个变量的值
# a = 1
# b = 2
# name = 'alex'

# why 为什么 三个场景
    # input
        # 用户输入的如果是a，那么就打印1，如果输入的是b就打印2，如果输入的是name，就打印alex
    # 文件
        # 从文件中读出的字符串，想转换成变量的名字
    # 网络
        # 将网络传输的字符串转换成变量的名字
# where 在哪儿用
# how 怎么用
hasattr
getattr
setattr
delattr
'''

#反射类中的变量
# class Foo:
#     school = 'oldboy'
#     country = 'China'
#     language = 'CHiness'
#     @classmethod
#     def class_method(cls):
#         print(cls.school)
#
#     @staticmethod
#     def static_method():
#         print('in static method')
#
#     def wahaha(self):
#         print('哇哈哈')
# 判断实现
# if inp == 'School':print(Foo.School)
# elif inp == 'Country':print(Foo.Country)
# elif inp == 'language':print(Foo.language)

# 反射实现
# while True:
#     inp = input('>>>')
#     if hasattr(Foo, inp): print(getattr(Foo, inp))

# 解析getattr方法
# getattr(变量名：命名空间，字符串：属于一个命名空间内的变量名)
# getattr(Foo,'school')  # Foo.School
# print(Foo.class_method)
# print(getattr(Foo,'class_method'))
# getattr(Foo,'class_method')()    # Foo.class_method()
# getattr(Foo,'static_method')()   # Foo.static_method()
# getattr(Foo,'wahaha')(1)  # Foo.wahaha(1)
# print(hasattr(Foo,'wahaha'))
# print(hasattr(Foo,'shuangwaiwai'))

#反射对象中变量
# 对象属性
# 普通方法
# class Foo:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def eating(self):
#         print('%s is eating'%self.name)
#
# alex = Foo('张三',25)
# if hasattr(alex,"name"): print(getattr(alex,'name'))
#
# getattr(alex,'eating')()


#反射模块中的变量
import os # os就是一个模块
#os.rename('./源码/__init__.py','./源码/__init__.py.bak')
# getattr(os,'rename')('./源码/__init__.py.bak','./源码/__init__.py')


# 反射本文件中的变量  分析过程
# a = 1
# b = 2
# name = 'alex'
# def qqxing():
#     print('qqxing')

# cls.xxx
# obj.xxx
# os.xxx

import sys
# print(sys.modules['__main__'])  # 本文件的命名空间
# print(sys.modules['__main__'].a)
# print([__name__]) # 变量，内置的变量
# print(sys.modules[__name__]) #反射本文件中变量 固定的使用这个命名空间
# print(getattr(sys.modules[__name__],'a'))
# print(getattr(sys.modules[__name__],'b'))
# print(getattr(sys.modules[__name__],'name'))
#
# foo = getattr(sys.modules[__name__],'Foo')()
# getattr(foo,'wahaha')()

#反射文件中的变量





#setattr
#delattr
class Foo:
    country = 'China'

def func():
    print('qqqqq')

setattr(Foo,'school','oldboy')  #接受3个参数  命名空间 ’变量名‘  变量值
print(getattr(Foo,'school'))
print(Foo.school)

setattr(Foo,'func',func)
Foo.func()

# delattr
print(Foo.__dict__)
delattr(Foo,'country')
print(Foo.__dict__)
















