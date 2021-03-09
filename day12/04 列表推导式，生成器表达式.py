# author:xuxk
# contact: 徐小康
# datetime:2021/3/3 13:24
# software: PyCharm

"""
文件说明：
"""
l1 = []
for num in range(1,101):
    l1.append(num)
print(l1)
'''
#列表推导式，一行代码代码几乎搞定你需要的任何列表
    循环模式 【变量（加工后的变量） for 变量 in iterable】
'''
# l = [i for i in range(1, 101)]
# print(l)
# # 循环模式
# l2 = ['python{}期'.format(i) for i in range(1,16)]
# print(l2)
#
# #筛选模式
# l3 = [i for i in range(1, 31) if i % 2 == 0]
# print(l3)
# # 30以内被3整除的数
# l4 = [i for i in range(1, 31) if i % 3 == 0]
# print(l4)
# l5 = [i*i for i in range(1, 31) if i % 3 == 0]
# print(l5)

#删选包含2个e的
names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
         ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]
print([j for i in names for j in i if j.count('e') == 2])
l1 =[name for i in names for name in i if name.count('e') == 2]
print(l1)

'''列表推导式
优点：一行解决，方便
缺点：容易着迷，不易排错，不能超过三次循环
'''

'''生成器表达式，将列表的[]换成（）'''
g = (j for i in names for j in i if j.count('e') == 2)
# print(g.__next__())
# print(g.__next__())

mcase = {'a':10,'b':34}
#字典 键值对互换
mcase_frequency = {mcase[k]: k for k in mcase}
print(mcase_frequency)

#返回平方并且集合去重
squared = {x**2 for x in [1,-1,2]}
print(squared)
