# -*- coding: utf-8 -*-
# @Time    : 2018/8/8 10:30
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 03 字典.py
# @Software: PyCharm

# dic = {'太白':{'name': '太白','age': 25, 'sex': '男',},
#        'name_list': ['王双','韩蕾','何青松',],
#        }
# dic = {'name': '太白', 'age': 18, 'sex': '男', 'job': 'IT'}

# 增
# 第一种：  有此key就改，无此key就添加
# dic['sex'] = '男'
# dic['name'] = 'alex'

# setdefault 有此key则不做任何操作但是给我返回对应的值，无此key则添加.
# dic.setdefault('sex')
# dic.setdefault('hobby','讲课')
# dic.setdefault('name','alex')
# print(dic.setdefault('name'))
# print(dic)

# 删

# pop 通过键去删除键值对，也有返回值,如果没有此键，并且设置了第二个参数，则不会报错，并且返回第二个参数。
# print(dic.pop('name'))
# print(dic.pop('name1',None))
# print(dic.pop('name1','没有此键....'))
# print(dic)

# clear 清空
# dic.clear()
# print(dic)

# popitem :3.5 之前随即删除某个键值对，3.6以后，删除最后一组键值对。有返回值.

# print(dic.popitem())
# print(dic)

# del
# 按照键删除键值对
# del dic['name']
# 删除整个字典
# del dic
# print(dic)

# 改
# 第一种：
# dic['age'] = 25
# print(dic)

# 两个字典 update
# dic = {"name":"jin","age":18,"sex":"male"}
# dic2 = {"name":"alex","weight":75}
# dic.update(dic2)  # 将dic2中的所有键值对覆盖并添加到dic中，dic2 不变。
# print(dic)
# print(dic2)
# dic.update(a='666',b='222',name='taibai')
# print(dic)
#查
# print(dic['name'])
# print(dic['name1']) # 没有这个报错

# print(dic.get('name'))
# print(dic.get('name1'))
# print(dic.get('name1','没有此键。。。。'))

# dic.keys()
# print(dic.keys())
# print(type(dic.keys()))  # 类似于列表的容器中
# l1 = list(dic.keys())  # 可以转化成list
# print(l1)
# for key in dic.keys():  # 可以遍历
#     print(key)
#
# #dic.values()  可转化成list，可遍历。
# print(dic.values())
# print(list(dic.values()))

#dic.items()  可转化成list，可遍历。
# print(dic.items())
# for i in list(dic.items()):
#     for j in i:
#         print(j)
# 分别赋值
# a,b = 10,20
# print(a,b)
# a,b = [10,20]
# print(a,b)
# a,b = [(1,2),(3,4)]
# print(a,b)
# a = 10
# b = 20
# a,b = b,a
# print(a,b)
''''练习'''
dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
#请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
#dic.update({'k4':'v4'})
# dic.setdefault('k4','v4')
# print(dic)
# 请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
# dic.update({"k1":'alex'})
# print(dic)
# 请在k3对应的值中追加一个元素 44，输出修改后的字典
# ss = dic.get('k3')
# ss.append(44)
# dic.update({'k3':ss})
# print(dic)
#dic.update(('k3': )
# 请在k3对应的值的第 1 个位置插入个元素 18，输出修改后的字典
# ss = dic.get('k3')
# ss.insert(0,18)
# dic.update({'k3':ss})
# print(dic)

# for i in dic.items():
#     #i = ('name', '太白')
#     #i = ('age', 18)
#     print(i)




# for k,v in dic.items():
#     #'''
#     #k,v = ('name', '太白')
#     #k,v = ('age', 18)
#     #....
#     #'''
#     print(k,v)

# for i in dic:
#     print(i)
# dict
# print(len(dic))

'''fromkeys  数据类型的补充时会给大家讲到~'''
# dic = dict.fromkeys('abcd','太白')
# print(dic) # {'a': '太白', 'b': '太白', 'c': '太白', 'd': '太白'}
#
# dic = dict.fromkeys([1, 2, 3],'太白')
# print(dic) # {1: '太白', 2: '太白', 3: '太白'}

'''其他操作'''