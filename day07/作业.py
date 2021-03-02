# -*- coding: utf-8 -*-
# @Time    : 2018/8/13 9:08
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 02 作业讲解.py
# @Software: PyCharm

# dic = dict.fromkeys([1,2,3],[])
# print(dic)
# print(id(dic[1]))
# print(id(dic[2]))
# print(id(dic[3]))

# dic = dict.fromkeys('1234','alex')
# dic['1'] = 'egon'
# print(dic)    #结果# {'1': 'egon', '2': 'alex', '3': 'alex', '4': 'alex'}


# dic = dict.fromkeys('1234',[])
# dic['1'] = 'egon'
# print(dic)      结果# {'1': 'egon', '2': [], '3': [], '4': []}


# dic = dict.fromkeys('1234',[])
# dic['2'].append('msr')
# print(dic)      结果 #{'1': ['msr'], '2': ['msr'], '3': ['msr'], '4': ['msr']}

# l1 = [1, 2, 3,['taibai',]]
# l2 = l1.copy()
# print(l1 is l2)  # 内存中两个列表不是一个。
# print(id(l1[1]))
# print(id(l2[1]))
# print(id(l1[-1]))
# print(id(l2[-1]))
# import copy
# l1 = [1, 2, 3,['taibai',]]
# l2 = copy.deepcopy(l1)
# print(id(l1))
# print(id(l2))
# print(id(l1[-1]))
# print(id(l2[-1]))
import copy
# d1 = {'name':"alex"}
# d2 = copy.deepcopy(d1)
# print(id(d2),id(d1))

# d1 = 'alex'
# d2 = copy.deepcopy(d1)
# print(id(d2),id(d1))

#
# 4，电影投票.程序先给出⼀个⽬前正在上映的电影列表.由⽤户给每⼀个电影投票.最终
# 将该⽤户投票信息公布出来 。（此题明天可以继续做）
# 要求：
# 1，用户输入序号，进行投票。比如输入序号
# 1，给金瓶梅投票1。
# 2，每次投票成功，显示给哪部电影投票成功。
# 3，退出投票程序后，要显示最终每个电影的投票数。
# 结果: {'⾦瓶梅': 99, '解救吴先⽣': 80, '美国往事': 6, '⻄⻄⾥的美丽传说': 23}
# lst = ['⾦瓶梅', '解救吾先⽣', '美国往事', '⻄⻄⾥的美丽传说']
# dic = {'⾦瓶梅': 0, '解救吾先⽣': 0, '美国往事': 0, '⻄⻄⾥的美丽传说': 0}
# print("'⾦瓶梅': %(⾦瓶梅)s, '解救吾先⽣': %(解救吾先⽣)s, '美国往事': %(美国往事)s\
#  , '⻄⻄⾥的美丽传说': %(⻄⻄⾥的美丽传说)s" %dic)
# while 1:
#     for index,name in enumerate(lst,1):
#         print('序号{0}:{1}'.format(index,name))
#     num = input('请输入你投票的电影序号：(Q或者q退出)').strip()
#     if num.isdigit() and ( 0 <int(num)<= len(lst)):
#         dic[lst[int(num) - 1]] += 1
#         print(lst[int(num)-1] + '投票成功')
#     elif num.upper() == 'Q': break
#     else:
#         print('没有此序号。。。。')
# print("'⾦瓶梅': %(⾦瓶梅)s, '解救吾先⽣': %(解救吾先⽣)s, '美国往事': %(美国往事)s\
#  , '⻄⻄⾥的美丽传说': %(⻄⻄⾥的美丽传说)s" %dic)


cars = ['鲁123','京333','黑3234','沪32332','鲁123','京333','黑3234','沪32332','鲁123','京333','黑3234']
locals = {'沪':'上海','黑':'黑龙江','鲁':'山东','京':'北京'}
# #结果 ｛‘黑龙江’:2,'上海'：3，‘鲁’：3....｝

# #{'上海': 0, '黑龙江': 0, '山东': 0, '北京': 0}
dic = {}
dic = dic.fromkeys(locals.values(),0)
for car in cars:
    if car[0] in locals:
        dic[locals[car[0]]] += 1

print(dic)

'''
3 干掉主播，现有主播收益信息 zhubo={'卢本伟':12200,'冯提莫':189999,'金老板':99999,'吴老板':25000000,'alex':126}
'''
# 计算主播平均收益
zhubo={'卢本伟':12200,'冯提莫':189999,'金老板':99999,'吴老板':25000000,'alex':126}
totalMoney = 0
for i in zhubo.values():
    totalMoney+= i
print(totalMoney/len(zhubo))
# 干掉收益小于平均值的主播
zhubo1 = {}
for k,v in zhubo.items():
    if v >= 5060464.8: zhubo1[k] = v
print(zhubo1)

#干掉卢本伟
zhubo.pop('卢本伟')
print(zhubo)




