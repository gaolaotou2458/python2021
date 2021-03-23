# author:xuxk
# contact: 徐小康
# datetime:2021/3/9 10:03
# software: PyCharm

"""
文件说明：
"""
# l1 = [1,2,3,5,6,7]
# tu1 = ('alex','太白', 'wusir', '女神')
# dic = {'name': '日天', 'age':28, 'hobby': 'tea', 'weight':100}
#
# for i in zip(l1,tu1,dic) :
#     print(i)

'''fliter过滤'''
# l1 = [i for i in range(10)]
# def func1(x):
#     return x % 2 == 0
# print(list(filter(func1,l1)))

'''map:回根据提供的函数对指定序列做映射，循环模式'''
# l1 = [1,2,3,4]
# l2 = [i**2 for i in l1]
# print(l2)
# def func2(x):
#     return x**2
# print(list(map(func2,l1)))

'''
    匿名函数 lambda表达式，一行函数
    普通函数 有且只有返回值的函数才可以用匿名函数进行简化 一行函数
'''
'''lambda'''
# f1 = lambda x:x*2
# print(f1(2))
#
# f2 = lambda x,y:x+y
# print(f2(2,3))
# # 匿名函数 不单独使用，多与内置函数结合。
# l2 = [(1,1000),(2,18),(4,250),(3,500)]
# print(sorted(l2,key=lambda x:x[1]))

dic = {'k1': 10, 'k2': 100, 'k3': 30}
#1,利用内置函数匿名函数将dic按照值进行排序。
print(sorted(dic, key=lambda x: dic[x]))
print(sorted(dic.items(), key=lambda x: x[1]))
# [1,5,7,4,8]
# 利用内置函数匿名函数 计算列表的每个数的2倍。
l1 = [1,5,7,4,8,12,15]
print(list(map(lambda x:x*2,l1)))
# [5,8,11,9,15]
# 利用内置函数匿名函数，将值大于10的留下来。
print(list(filter(lambda x: x > 10, l1)))
