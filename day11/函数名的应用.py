# author:xuxk
# contact: 徐小康
# datetime:2021/3/2 9:11
# software: PyCharm

"""
文件说明：
"""
# def func1():
#     print(666)

# 1,函数名就是内存的地址
# print(func1())

# 2. 函数名可以作为变量
# f1 = func1
# f2 = f1
# f2()


# 3 函数名可以作为函数的参数
def func1():
    print(666)


def func2(x):
    #x()
    print(x)
    x()


#func2(func1)

# a='太白'
# func2(a)

# print(func1)
#
# def wrapper():
#     def inner():
#         print('inner')
#         return 666
#     return inner
# ret = wrapper()
# ret()
# def func2():
#     print('in func2')
#
# def func3(x):
#     print('in func3')
#     return x
#
# f1 = func3(func2)
# f1()

'''函数名可以作为容器类型的元素'''
# a = 2
# b = 3
# c = 5
# l1 = [a,b,c]

# def func1():
#     print('in func1')
#
# def func2():
#     print('in func2')
#
# def func3():
#     print('in func3')
#
# def func4():
#     print('in func4')
#
# l1 = [func1,func2,func3,func4]
# for func in l1:
#     func()
# 向上面的函数名这种，第一类对象

'''
globals() 返回全局变量的一个字典 
locals() 返回当前位置的  局部变量的字典
'''
# def func1():
#     a = 2
#     b = 3
#     # print(globals())
#     # print(locals())
#     def inner():
#         c = 5
#         d = 6
#         print(globals())
#         print(locals())
#     inner()
# # print(globals())
# # print(locals())
# func1()