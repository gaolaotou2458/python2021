# # -*- coding: utf-8 -*-
# # @Time    : 2018/8/7 9:33
# # @Author  : 骑士计划
# # @Email   : customer@luffycity.com
# # @File    : 02 作业讲解.py
# # @Software: PyCharm
#
# day3作业及默写
#
# 1，有变量name = "aleX leNb" 完成如下操作：
name = "aleX leNb"
# 1)	移除 name 变量对应的值两边的空格,并输出处理结果
#print(name.strip())
# 2)	移除name变量左边的"al"并输出处理结果
#print(name.lstrip('al'))
# 3)	移除name变量右面的"Nb",并输出处理结果
#print(name.rstrip('Nb'))
# 4)	移除name变量开头的a"与最后的"b",并输出处理结果
#print(name.strip('ab'))
# 5)	判断 name 变量是否以 "al" 开头,并输出结果
#print(name.startswith('al'))
# 6)	判断name变量是否以"Nb"结尾,并输出结果
# 7)	将 name 变量对应的值中的 所有的"l" 替换为 "p",并输出结果
#print(name.replace('l','p'))
# 8)	将name变量对应的值中的第一个"l"替换成"p",并输出结果
# 9)	将 name 变量对应的值根据 所有的"l" 分割,并输出结果。
# 10)	将name变量对应的值根据第一个"l"分割,并输出结果。
# 11)	将 name 变量对应的值变大写,并输出结果
# 12)	将 name 变量对应的值变小写,并输出结果
# 13)	将name变量对应的值首字母"a"大写,并输出结果
#print(name.capitalize())
# 14)	判断name变量对应的值字母"l"出现几次，并输出结果
#print(name.count('l'))
# 15)	如果判断name变量对应的值前四位"l"出现几次,并输出结果
#print(name[::5].count('l'))
# 16)	从name变量对应的值中找到"N"对应的索引(如果找不到则报错)，并输出结果
#print(name.find('N'))
# 17)	从name变量对应的值中找到"N"对应的索引(如果找不到则返回-1)输出结果
#print(name.index('N'))
# 18)	从name变量对应的值中找到"X le"对应的索引,并输出结果
#print(name.index('X le'))
# 19)	请输出 name 变量对应的值的第 2 个字符?
# print(name[1])
# 20)	请输出 name 变量对应的值的前 3 个字符?
# print(name[:3])
# 21)	请输出 name 变量对应的值的后 2 个字符?
# print(name[-2:])
# 22)	请输出 name 变量对应的值中 "e" 所在索引位置?
# print(name.index('e'))
# print(name.index('e',name.index('e')+1,))





# 2，有字符串s = "123a4b5c"
s = "123a4b5c"
#
# 1)通过对s切片形成新的字符串s1,s1 = "123"
# 2)通过对s切片形成新的字符串s2,s2 = "a4b"
# 3)通过对s切片形成新的字符串s3,s3 = "1345"
#print(s[0::2])
# 4)通过对s切片形成字符串s4,s4 = "2ab"
#print(s[1:-1:2])
# 5)通过对s切片形成字符串s5,s5 = "c"
#print(s[-1])
# 6)通过对s切片形成字符串s6,s6 = "ba2"
#print(s[1:-1:2][::-1])
#
# 3，使用while和for循环分别打印字符串s="asdfer"中每个元素。
#
# 4，使用for循环对s="asdfer"进行循环，但是每次打印的内容都是"asdfer"。
#
# 5，使用for循环对s="abcdefg"进行循环，每次打印的内容是每个字符加上sb，	例如：asb, bsb，csb,...gsb。
# 6，使用for循环对s="321"进行循环，打印的内容依次是："倒计时3秒"，"倒计时2秒"，"倒计时1秒"，"出发！"。
# s = '321'
# for i in s:
#     print('倒计时{}秒'.format(i))
# print('出发！')

#
#
# 7，实现一个整数加法计算器(两个数相加)：
# 如：content = input("请输入内容:") 用户输入：5+9或5+ 9或5 + 9，然后进行分割再进行计算。

# content = input("请输入内容:").strip()  # 5+9   100      + 99     22+   34
# # # 方法一：
# plus_index = content.find('+')
# num1 = content[:plus_index]  # '5   '
# num2 = content[plus_index+1:] # '    9'
# result = int(num1) + int(num2)
# print(result)
# print(int('      5'),type(int('      5')))
# 方法二：
# content = input("请输入内容:").strip()  # 5+9   100      + 99     22+   34
# num_list = content.split('+')   # ['5   ', '      9']
# result = int(num_list[0]) + int(num_list[1])

# 8，升级题：实现一个整数加法计算器（多个数相加）：
# 如：content = input("请输入内容:") 用户输入：5+9+6 +12+  13，然后进行分割再进行计算。
'''
context = '5+9+6 +12+  13'
print(context.replace(' ',''))
list = context.split('+')
print(list)
count = 0
for i in list:
    count += int(i)
print(count)
'''
#
# 9，计算用户输入的内容中有几个整数（以个位数为单位）。
# 如：content = input("请输入内容：")   # 如 fhda234slfh9
# content = input("请输入内容：").strip()
# count = 0
# for i in content:
#     if i.isdigit():
#         count += 1
# print(count)






# 10、写代码，完成下列需求：
# 用户可持续输入（用while循环），用户使用的情况：
# 输入A，则显示走大路回家，然后在让用户进一步选择：
# 是选择公交车，还是步行？
# 选择公交车，显示10分钟到家，并退出整个程序。
# 选择步行，显示20分钟到家，并退出整个程序。
# 输入B，则显示走小路回家，并退出整个程序。
# 输入C，则显示绕道回家，然后在让用户进一步选择：
# 是选择游戏厅玩会，还是网吧？
# 选择游戏厅，则显示 ‘一个半小时到家，爸爸在家，拿棍等你。’并让其重新输入A，B,C选项。
# 选择网吧，则显示‘两个小时到家，妈妈已做好了战斗准备。’并让其重新输入A，B,C选项。
#
# 11、写代码：计算 1 - 2 + 3 ... + 99 中除了-88以外所有数的总和？

# 1 - 2 + 3 ... + 99

# count = 1
# sum1 = 0
#
# while count < 100:
#     if count == 88:
#         count += 1
#     #count 89
#     if count % 2 == 0:
#         sum1 -= count
#     else:
#         sum1 += count
#     count += 1
# print(sum1)




# 16、制作趣味模板程序需求：等待⽤户输⼊名字、地点、爱好，根据⽤户的名字和爱好进⾏任意现实 如：敬爱可亲的xxx，最喜欢在xxx地⽅⼲xxx
#
# 17、等待⽤户输⼊内容，检测⽤户输⼊内容中是否包含敏感字符？如果存在敏感字符提示“存在敏感字符请重新输⼊”，并允许⽤户重新输⼊并打印。敏感字符：“⼩粉嫩”、“⼤铁锤”
#
#
# 明日默写内容：
# 分别用while，for循环输出字符串s = input（"你想输入的内容"）的每一个字符。
context = 'input（"你想输入的内容"）'
# for i in context:
#     print(i)

s =0
while s < len(context) :
    print(context[s])
    s+=1
