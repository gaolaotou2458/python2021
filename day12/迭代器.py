# author:xuxk
# contact: 徐小康
# datetime:2021/3/3 9:40
# software: PyCharm

"""
文件说明：
"""
# l1 = [1,2,3]
# iter1 = iter(l1)
# while 1:
#     try:
#         print(iter1.__next__())
#     except StopIteration:
#         break

# def func1(x):
#     x += 1
#     return x
# func1(5) #函数的执行命令，并且接受函数的返回值
#
# print(func1(5))

# 生成器函数
# x生成器对象
# def func2(x):
#     x += 1
#     print(1111)
#     yield x
#     print(2222)
#
# g_obj = func2(5)
# print(g_obj.__next__())
# print(g_obj.__next__())
# 一个next 对应一个 yield
# yield return
# return 结束函数，给函数的执行者返回值
# yield 不会结束函数，一个next对应一个yield，给  生成器对象.__next__() 返回值。
# 区别1：内存级别的区别。
# 迭代器是需要可迭代对象进行转化。可迭代对象非常占内存。
# 生成器直接创建，不需要转化，从本质就节省内存。
# def func1():
#     for i in range(1000000):
#         yield i
# g1 = func1()
# for i in range(50):
#     print(g1.__next__())

# send 与 next

# def func1():
#     # print(1)
#     count = yield 6
#     print(count)
#     # print(2)
#     #count1 = \
#     yield 7
#     #print(count1)
#     # print(3)
#     yield 8
#
# g = func1()
# next(g)
# g.send('alex')
# next(g)
# g.send('alex')
# g.send('太白')
# g.send('太白')

# send 与next一样，也是对生成器取值（执行一个yield）的方法。
# send 可以给上一个yield 传值。
# 第一次取值永远都是next。
# 最后一个yield 永远也得不到send传的值。


# def cloth1(n):
#     for i in range(n+1):
#         print('衣服%s号' % i)
# cloth1(100000)
def cloth2(n):
    for i in range(1,n+1):
        yield '衣服%s号' % i
g = cloth2(10000)
for i in range(50):
    print(g.__next__())
for i in range(50):
    print(g.__next__())