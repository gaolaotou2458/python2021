# author:xuxk
# contact: 徐小康
# datetime:2021/3/1 8:43
# software: PyCharm


def func1():
    print(111)


'''
再函数定义是，在*位置参数，聚合
*args 将所有的实参的位置参数聚合到一个元组，并将元素赋值给args
**kwargs 将实参的所有关键字参数，赋值给kwargs
'''


def sum1(*args, **kwargs):
    print(args)
    print(kwargs)


#
# sum1(1, 2, 3, 4, name='alex', age=1000)


def wn_sum1(*args):
    return args[0] + args[1]


l1 = [1, 2, 3]
l2 = [111, 22, 33, 'alex']


# print(wn_sum1(l2, l1))


def func2(*args, **kwargs):
    # print(args)
    print(kwargs)


# func2(*l1, *l2)
# func2(*(1, 2, 3), *('alex', 'sb'))
# func2(**{'name': 'alex', 'age': 100})  #= func2(name='alex',age=1000)

# 形参得顺序
# 位置参数，默认参数，*args,**kwargs
# 位置参数在前，默认参数在后
def func3(a, sex='男'):
    print(a)
    print(sex)


# func3(100,'女')

# 默认参数放在args前面，不然会被被替换
def func4(a, b, sex='男', *args):
    print(a, b, sex)


#func4(1, 2, 333, 4, 55, 66)


# 位置参数，*args, 默认参数 **kwargs
#最全的参数位置
def func5(a, b, *args, sex='男', **kwargs, ):
    print(a, b)
    print(sex)
    print(args)
    print(kwargs)


func5(100, 200, 1, 2, 34, 5, 6, sex='nv', name='alex', age=1000)
