# author:xuxk
# contact: 徐小康
# datetime:2021/2/23 15:08
# software: PyCharm

"""
文件说明：dict字典
不可变（可哈希）的数据类型：int，str，bool，tuple。
可变（不可哈希）的数据类型：list，dict，set。
"""
#创建字典的几种方式：
# 方式1:
# dic = dict((('one',1),('tow',2),('three',3)))
# print(dic)
# # 方式2:
# dic = dict(one=1,two=2,three=3)
# print(dic)
# # 方式3:
# dic = dict({'one':1,'two':2,'three':3})
# print(dic)
#
# # 方式5: 后面会讲到先了解
# dic = dict(zip(['one', 'two', 'three'],[1, 2, 3]))
# print(dic)
#
# # 方式6: 字典推导式 后面会讲到
# dic = { k: v for k,v in [('one', 1),('two', 2),('three', 3)]}
# print(dic)
#
# # 方式7:利用fromkey后面会讲到。
# dic = dict.fromkeys('abcd','太白')
# print(dic)  # {'a': '太白', 'b': '太白', 'c': '太白', 'd': '太白'}

'''验证字典的合法性'''
#dic = {123: 456, True: 999, "id": 1, "name": 'sylar', "age": 18, "stu": ['帅哥', '美⼥'], (1, 2, 3): '麻花藤'}
# print(dic[123])
# print(dic[True])
# print(dic['id'])
# print(dic['stu'])
# print(dic[(1,2,3)])


# 不合法
#dic = {[1, 2, 3]: '周杰伦'} # list是可变的. 不能作为key
#dic = {{1: 2}: "哈哈哈"} # dict是可变的. 不能作为key
#dic = {{1, 2, 3}: '呵呵呵'} # set是可变的, 不能作为key

'''字典的常用操作方法'''
'''增'''
# 通过键值对直接增加
'''
dic = {'name': '太白', 'age': 18}
dic['weight'] = 75 # 没有weight这个键，就增加键值对
print(dic) # {'name': '太白', 'age': 18, 'weight': 75}
dic['name'] = 'barry' # 有name这个键，就成了字典的改值
print(dic) # {'name': 'barry', 'age': 18, 'weight': 75}
'''
# setdefault
# dic = {'name': '太白', 'age': 18}
# dic.setdefault('height',175) # 没有height此键，则添加
# print(dic) # {'name': '太白', 'age': 18, 'height': 175}
# dic.setdefault('name','barry') # 有此键则不变
# print(dic) # {'name': '太白', 'age': 18, 'height': 175}
# #它有返回值
# dic = {'name': '太白', 'age': 18}
# ret = dic.setdefault('name')
# print(ret)  # 太白

'''删除'''
# pop 通过key删除字典的键值对，有返回值，可设置返回值。
dic = {'name': '太白', 'age': 18}
# ret = dic.pop('name')
# print(ret,dic) # 太白 {'age': 18}
# ret1 = dic.pop('n',None)
# print(ret1,dic) # None {'name': '太白', 'age': 18}

#popitem 3.5版本之前，popitem为随机删除，3.6之后为删除最后一个，有返回值
# dic = {'name': '太白', 'age': 18}
# ret = dic.popitem()
# print(ret,dic) # ('age', 18) {'name': '太白'}

#clear 清空字典
# dic = {'name': '太白', 'age': 18}
# dic.clear()
# print(dic) # {}

# del
# 通过键删除键值对
# dic = {'name': '太白', 'age': 18}
# del dic['name']
# print(dic) # {'age': 18}
#删除整个字典
# del dic
'''改'''
# 通过键值对直接改
# dic = {'name': '太白', 'age': 18}
# dic['name'] = 'barry'
# print(dic) # {'name': 'barry', 'age': 18}
#
# # update
# dic = {'name': '太白', 'age': 18}
# dic.update(sex='男', height=175)
# print(dic) # {'name': '太白', 'age': 18, 'sex': '男', 'height': 175}
#
# dic = {'name': '太白', 'age': 18}
# dic.update([(1, 'a'),(2, 'b'),(3, 'c'),(4, 'd')])
# print(dic) # {'name': '太白', 'age': 18, 1: 'a', 2: 'b', 3: 'c', 4: 'd'}
# print(type([(1, 'a'),(2, 'b'),(3, 'c'),(4, 'd')]))
# print(type((1,'a')))

'''查'''