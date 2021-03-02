# author:xuxk
# contact: 徐小康
# datetime:2021/3/1 13:30
# software: PyCharm

"""
文件说明：
"""

# def func1():
#     print(1111)
#
# def func2():
#     print(222)
#     func1()
#     print(333)
#
# print(666)
# func2()
# print(555)

# def func1():
#     print(222)
#     def func2():
#         print(333)
#     print(111)
#     func2()
#     print(666)
# func1()

'''global
局部名称空间， 对全局空间的变量可以引用，但是不能改变

# 如果你在局部名称空间 对一个变量进行修改，那么解释器会认为你的这个变量在局部中已经定义了，
# 但是对于上面的例题，局部中没有定义，所以他会报错，
global:
    1.在局部名称空间申明一个全局变量
    2.在局部名称空间可以对全局变量进行修改
'''
# count = 0
#
#
# def func1():
#     global count
#     count += 1 #UnboundLocalError: local variable 'count' referenced before assignment
#     print(count)
#
#
# func1()
#
#
# def func2():
#     global name
#     name = 'alex'
#
#
# func2()
# print(name)

'''nonlocal
 子函数对父函数的变量进行修改。
 此变量不能是全局变量
 # 在局部作用域中，对父级作用域（或者更外层作用域非全局作用域）的变量进行引用和修改，
# 并且引用的哪层，从那层及以下此变量全部发生改变。
'''

# def func1():
#     count = 666
#     def func2():
#         nonlocal count
#         count +=1
#         print(count)
#     func2()
# func1()

# 在局部作用域中，对父级作用域（或者更外层作用域非全局作用域）的变量进行引用和修改，
# 并且引用的哪层，从那层及以下此变量全部发生改变。
def func1():
    count = 666
    def inner():
        print(count)
        def func2():
            nonlocal count
            count += 1
            print('func2',count)
        func2()
        print('inner',count)
    inner()
    print('func1',count)
func1()