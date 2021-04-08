# -*- coding: utf-8 -*-
# @Time    : 2018/8/31 15:31
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 7.试题讲解.py
# @Software: PyCharm

# def outer():
#     name = 'alex'
#     print(name)
#     def inner():
#         # name = 'wupeiqi'
#         print(name)
#     print(inner.__closure__)  # inner是一个闭包
#
# outer()

# 闭包 ： 装饰器
    #     做缓存
# from urllib.request import urlopen
#
#
# # 爬虫 ： 网页有很多数据，把网页上的数据爬下来
# def get_url(url):
#     ret = urlopen(url)
#     content = ret.read().decode('utf-8')
#     def get():return content
#     return get
#
# get = get_url('http://www.cnblogs.com/Eva-J/p/7277026.html')
# get()

# def f(x,l=[]):
#     for i in range(x):
#         l.append(i*i)
#     print(l)
#
# f(2)  #[0, 1]
# f(3,[3,2,1]) #[3, 2, 1, 0, 1, 4]
# f(3) #[0, 1, 0, 1, 4]


# 写出下面代码的输出结果
# l = [1,2,3]
# d = {'a':7,"b":8}
#
# def f(arg1,arg2,*args,**kwargs):
#     print(arg1,arg2,args,kwargs)
#
# f(1,2,*l,q="winning",**d)  #1,2,(1,2,3),{"q":"winning".'a':7,"b":8}

'''输出返回结果'''
# 代码题目（70分）
# for i in range(0,5,2):
#     print(i)  # 0 2 4

'''1有列表 a = ["7net","www.7net","www.septnet","7net","www"]'''
# a = ["7net","www.7net","www.septnet","7net","www"]
#
# b = [i for i in a if "7net" not in i]
# print(b)

'''2.
l = ['20','10','3','15','32'] 从小到大排序'''
# l = ['20','10','3','15','32']
# print([str(j) for j in sorted([int(i) for i in l])])

'''
3 l = ['班级20','班级10','班级3','班级15','班级32']
按照数字的顺序从小到大排序，不改变元列表
'''
# l = ['班级20','班级10','班级3','班级15','班级32']
# def test(i):
#     print(i[2:])
#     return int(i[2:])
# print(sorted(l,key=test))

'''4 l1 = ['alex','Wusir','老男孩','太白'] 用列表推导式改成
['alex0','Wusir1','老男孩2','太白3']'''
# l1 = ['alex','Wusir','老男孩','太白']
#
# print([value+str(key) for (key,value) in enumerate(l1,0)])

'''5 现有两个元组(('a'),('b'),('c'),('d'))
请使用匿名函数和内置函数生成列表[{'a':'c'},{'b':'d'}}]
'''
# t1 = ('a'),('b')
# t2 = ('c'),('d')
# print(list(map(lambda t:{t[0]:t[1]},(zip(t1,t2)))))


'''
现有列表 alist = [3,1,-4,-2],只能找元素的绝对值大小排序并获得每个元素的平方
'''
alist = [3,1,-4,-2]
print(list(map(lambda x:x**2,sorted(alist,key=abs))))

# print(type((3)))
# print(type((3,)))

# 'abdaadf'
# dic = {}
# for i in 'abdaadf':
#     if i in dic:
#         dic[i] +=1
#     else:
#         dic[i] = 1
# res = []
# for k in dic:
#     res.append('%s:%s'%(k,dic[k]))
# print('|'.join(res))


# dic = {}
# for i in 'abdaadf':
#     dic[i] = dic[i] +1 if i in dic else 1
# print('|'.join(['%s:%s'%(k,dic[k]) for k in dic]))

# str1 = 'abdaadf'
# print(''.join(['%s:%s|'%(i,str1.count(i)) for i in set(str1)])[:-1])

# for
dicta = {"a":1,"b":2,"c":3,"d":4,"f":"hello"}  # a b c d f
dictb = {"b":3,"d":5,"e":7,"m":9,"k":"world"}
# for
# for k in dicta:
#     if k in dictb:
#         dicta[k] += dictb[k]
# # for
# for k in dictb:
#     if k not in dicta:
#         dicta[k] = dictb[k]
# print(dicta)

for k in dicta:
    if k in dictb:
        dicta[k] += dictb[k]
        dictb.pop(k)
dicta.update(dictb)
print(dicta)

# def func1(a,b):
#     for i in b:
#         if i in a:
#             a[i] += b[i]
#         else:
#             a[i] = b[i]
#     return a
# dicta = {"a":1,"b":2,"c":3,"d":4,"f":"hello"}
# dictb = {"b":3,"d":5,"e":7,"m":9,"k":"world"}
# print(func1(dicta,dictb))

# x = {'a':1,'b':2,'c':3,'d':4,'f':'ew'}
# y = {'a':1,'b':2,'c':3,'e':4,'f':'wefew'}
#
# def func(a,b):
#     dic = dict.fromkeys(a.keys() | b.keys())
#     d =  {i: a[i]+b[i] if a.get(i) and b.get(i) else a[i] if a.get(i) else b[i]   for i in dic}
#     print(d)
# func(x,y)

# 16、写函数，完成给一个列表去重的功能。（不能使用set集合）（8分）
# lst = [1,2,3,4,5,1,2,3,4]
# new_lst = []
# for i in new_lst:
#     if i not in new_lst:
#         new_lst.append(i)
