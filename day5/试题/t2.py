# author:xuxk
# contact: 徐小康
# datetime:2021/2/24 8:48
# software: PyCharm

"""
文件说明：
"""
# dic = {
#     'name':'汪峰',
#     'age':48,
#     'wife':[{'name':'国际章','age':38}],
#     'children':{'girl_first':'小苹果','girl_second':'小怡','girl_three':'顶顶'}
# }
#
# #1. 获取汪峰的名字。
# print(dic.get('name'))
# #2.获取这个字典：{'name':'国际章','age':38}。
# print(dic.get('wife')[0])
# #3. 获取汪峰妻子的名字。
# print(dic.get('wife')[0].get('name'))
# #4. 获取汪峰的第三个孩子名字。
# print(dic.get('children').get('girl_three'))


# dic1 = {
#  'name':['alex',2,3,5],
#  'job':'teacher',
#  'oldboy':{'alex':['python1','python2',100]}
#  }
# 1，将name对应的列表追加⼀个元素’wusir’。
#dic1.get('name').append('wusir')
# 2，将name对应的列表中的alex⾸字⺟⼤写。
#dic1.get('name')[0] = dic1.get('name')[0].upper()
# 3，oldboy对应的字典加⼀个键值对’⽼男孩’,’linux’。
#dic1.get('oldboy').setdefault('老男孩','linux')
# 4，将oldboy对应的字典中的alex对应的列表中的python2删除
# dic1.get('oldboy').get('alex').pop(1)
# print(dic1)


l1 = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
dic = {}
# 1.将所有大于66的值保存至字典，第一个key中，将小于66的值保存至第二个key的值中。
# v1 = []
# v2 = []
# for key in l1:
#     if key > 66:
#         v1.append(key)
#     else:
#         v2.append(key)
# dic['k1'] = v1
# dic['k2'] = v2
# print(dic)


#4.有字符串
#k:1|k1:2|k2:3|k3:4 处理成{'k':1,'k1':2}
s = 'k:1|k1:2|k2:3|k3:4'
s1 = s.split('|')
dic = {}
print(s1)
for i in s1:
    s2 = i.split(':')
    key = s2[0]
    value = s2[1]
    dic[key] = value
print(dic)

