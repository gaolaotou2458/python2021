# # -*- coding: utf-8 -*-
# # @Time    : 2018/8/8 9:07
# # @Author  : 骑士计划
# # @Email   : customer@luffycity.com
# # @File    : 02 作业讲解.py
# # @Software: PyCharm
# day4作业及默写
# 1，写代码，有如下列表，按照要求实现每一个功能
#
#li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# 1)计算列表的长度并输出
# 2)列表中追加元素"seven", 并输出添加后的列表
# 3)请在列表的第1个位置插入元素
# "Tony", 并输出添加后的列表
# li.insert(1,'Tony')
# print(li)
# 4)请修改列表第2个位置的元素为
# "Kelly", 并输出修改后的列表
# 5)请将列表l2 = [1, "a", 3, 4, "heart"]
# 的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
# l2 = [1, "a", 3, 4, "heart"]
# li.extend(l2)
# print(li)
# 6)请将字符串s = "qwert"
# 的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
# li.extend('qwert')
# print(li)
# 7)请删除列表中的元素
# "alex", 并输出添加后的列表
# 8)请删除列表中的第2个元素，并输出删除的元素和删除元素后的列表
# print(li.pop(1))
# print(li)
# 9)请删除列表中的第2至4个元素，并输出删除元素后的列表
# del li[1:5]
# print(li)
# 10)请将列表所有得元素反转，并输出反转后的列表
# print(li[::-1])
# 11)请计算出
# "alex"
# 元素在列表li中出现的次数，并输出该次数。
# print(li.count('alex'))
#
# 2，写代码，有如下列表，利用切片实现每一个功能
#
li = [1, 3, 2, "a", 4, "b", 5, "c"]
# 1)通过对li列表的切片形成新的列表l1, l1 = [1, 3, 2]
#print(li[0:3])
# 2)通过对li列表的切片形成新的列表l2, l2 = ["a", 4, "b"]
#print(li[3:6])
# 3)通过对li列表的切片形成新的列表l3, l3 = ["1,2,4,5]
#print(li[::2])
# 4)通过对li列表的切片形成新的列表l4, l4 = [3, "a", "b"]
#print(li[1:-2:2])
# 5)通过对li列表的切片形成新的列表l5, l5 = ["c"]
#print(li[-1:])
# 6)通过对li列表的切片形成新的列表l6, l6 = ["b", "a", 3]
#print(li[-3::-2])
#
# 3, 写代码，有如下列表，按照要求实现每一个功能。
#
lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# 1)将列表lis中的"tt"变成大写（用两种方式）。
# lis[3][2][1][0] = 'TT'
# lis[3][2][1][0] = lis[3][2][1][0].upper()


# 2)将列表中的数字3变成字符串"100"（用两种方式）。
# lis[1] = '100'
# lis[3][2][1][1] = '100'
# lis[3][2][1][1] = str(lis[3][2][1][1] + 97)
# print(lis)
# 3)将列表中的字符串
# "1"
# 变成数字101（用两种方式）。
#
# 4, 请用代码实现：
#
# li = ["alex", "eric", "rain"]
# 利用下划线将列表的每一个元素拼接成字符串"alex_eric_rain"
# li = "_".join(li)
# print(li)



# 5，利用for循环和range打印出下面列表的索引。
#
li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# for i in range(0,len(li)):
#     print(li[i])
# 6，利用for循环和range找出100以内所有的偶数并将这些偶数插入到一个新列表中。
# ss =[]
# for i in range(0,len(li)):
#     ss.append(li[i])
# print(ss)
#
# 7，利用for循环和range
# 找出50以内能被3整除的数，并将这些数插入到一个新列表中。
# ss =[]
# for i in range(0, 51):
#     if (i % 3 == 0):
#         ss.append(i)
# print(ss)
# 8，利用for循环和range从100
# ~1，倒序打印。
# for i in range(0,100):
#     print(100-i)
# 9，利用for循环和range从100
# ~10，倒序将所有的偶数添加到一个新列表中，然后对列表的元素进行筛选，将能被4整除的数留下来。
# ss = []
# for i in range(0,100):
#     if((100-i) % 2 ==0): ss.append(i)
# print(ss)
#
# for i in ss:
#     if(i % 4 != 0): ss.remove(i)
# print(ss)
# 10，利用for循环和range，将1 - 30
# 的数字一次添加到一个列表中，并循环这个列表，将能被3整除的数改成 *。
# ss = []
# for i in range(1,31):
#     if(i % 3 == 0):
#         i = '*'
#     ss.append(i)
# print(ss)
# 11，查找列表li中的元素，移除每个元素的空格，并找出以
# "A"
# 或者
# "a"
# 开头，并以
# "c"
# 结尾的所有元素，并添加到一个新列表中, 最后循环打印这个新列表。
li = ["TaiBai ", "alexC", "AbC ", "egon", " riTiAn", "WuSir", "  aqc"]
# ss = []
# for i in li:
#     i = i.strip()
#     if(i.capitalize().startswith('A')  and i.endswith('c')):
#         ss.append(i)
# print(ss)
# 12，开发敏感词语过滤程序，提示用户输入评论内容，如果用户输入的内容中包含特殊的字符：
# 敏感词列表li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
# 则将用户输入的内容中的敏感词汇替换成等长度的 *（苍老师就替换 ** *），并添加到一个列表中；
# 如果用户输入的内容没有敏感词汇，则直接添加到上述的列表中。
# li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
# con_list = []
# while 1:
#     comment = input('请输入评论：').strip()  # ***", "***", "武藤兰", "波多野结衣"
#     if comment.upper() == 'Q': break
#     for i in li:
#         comment = comment.replace(i,'*'*len(i))  # ***", "***", "武藤兰", "*****"
#     con_list.append(comment)
# print(con_list)
#
# s1 = '太白 fkjsdaklfjl 太白fkdsjlafj太白'
# c1 = s1.replace('alex','男神')
# print(c1)

# 13，有如下列表
li = [1, 3, 4, "alex", [3, 7, 8, "TaiBai"], 5, "RiTiAn"]
# 循环打印列表中的每个元素，遇到列表则再循环打印出它里面的元素。
# 我想要的结果是：
# 1
# 3
# 4
#"alex"
# 3
# 7,
# 8
# "TaiBai"
# 5
# ritian








# 明日默写内容
# 1，将列表的增删改查不同的方法全部写出来，
# 例如：增：有三种，append：在后面添加。Insert按照索引添加，
# expend：迭代着添加。
# 2，默写第, 13
# 题的实现的代码。
#

# for i in li:
#     if type(i) == list:
#         for j in i:
#             print(j)
#     else:
#         print(i)