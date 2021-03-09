# -*- coding: utf-8 -*-
# @Time    : 2018/8/14 16:41
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : day08 作业讲解.py
# @Software: PyCharm
# import os
# # with open('a1',encoding='utf-8',) as f1,\
# #     open('a1.bak',encoding='utf-8',mode='w') as f2:
# #     for line in f1:
# #         if line.strip() == '我说的都是真的。哈哈':
# #             n_line = '你们就信吧\n' + line
# #             f2.write(n_line)
# #         else:
# #             f2.write(line)
# # os.remove('a1')
# # os.rename('a1.bak','a1')



# [{'name':'apple','price':10,'amount':3},{'name':'tesla','price':1000000,'amount':1}......]
# l1 = []
#
# with open('a', encoding='utf-8') as f1:
#     for line in f1:
#         if line.strip():
#             line_list = line.strip().split()  # [apple,10,3,2018]
#             print(line_list)
#             dic = {'name':line_list[0],'price':line_list[1],'amount':line_list[2],'year':line_list[3]}
#             l1.append(dic)
# print(l1)
# name_list = ['name','price','amount','year', '备注']
# l1 = []
# with open('a', encoding='utf-8') as f1:
#     for line in f1:
#         if line.strip():
#             line_list = line.strip().split()  # [apple,10,3,2017]
#             dic = {}
#             for index in range(len(name_list)):
#                 dic[name_list[index]] = line_list[index]
#             l1.append(dic)
# print(l1)
#print('a'+'b'+1)
#
# for i in range(3):
#     print(i)
# print('abcd'.replace('ab','cd'))

# print(1> 2 and 3 or 6)
# a= ('alex')
# print(type(a))
# dic = {}
# dic.fromkeys('abc',666)
# print(dic)

#讲 list3转成List4
list3=[
        {'name':'alex','hobby':'抽烟'},
        {'name':'alex','hobby':'喝酒'},
        {'name':'alex','hobby':'烫头'},
        {'name':'alex','hobby':'泡妞'},
        {'name':'阿三','hobby':'唱歌'},
        {'name':'阿三','hobby':'街舞'},
        {'name':'李四','hobby':'CS'}
    ]
def func1():

    list4 = []
    dic = {'name':0,'hobby_list':[]}
    set1 = set()
    for i in list3:
        set1.add(i.get('name'))
    for i in set1:
        list4.append(i)
    dic1 = {}
    dic1 = dic1.fromkeys(list4,dic)
    dic2 = {}


def func2():
    set1 = set()
    for i in list3: set1.add(i.get('name'))
    dic = {}
    for i in set1: dic[i] = {'name': i, 'hobby_list': []}
    for i in list3: dic[i.get('name')]['hobby_list'].append(i.get('hobby'))
    list4 = list(dic.values())
    print(list4)
func2()

#print(dic2)
#
# list5 = []
# for i in list3:
#     if i.get('name')  in set1:
#        print(dic1.get(i.get('name'))['hobby_list'])
        #dic1.get(i.get('name')).get('hobby_list').append(i.get('hobby'))
    #list5.append(dic1)
#print(list4)
