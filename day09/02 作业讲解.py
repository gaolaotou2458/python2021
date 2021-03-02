# # -*- coding: utf-8 -*-
# # @Time    : 2018/8/16 9:24
# # @Author  : 骑士计划
# # @Email   : customer@luffycity.com
# # @File    : 02 作业讲解.py
# # @Software: PyCharm
# day9 作业及默写
# 1，整理函数相关知识点,写博客。
#
# 2，写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
# def func(l1): return l1[1::2]


# 3，写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
# def func2(l) :
#     return len(l)>5
# print(func2('12345'))

# 4，写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。

# def func4(l):
#     if len(l) > 2:
#         l1 = l[:2]
#     else:
#         l1 = l
#     return l1
# print(func4([1,]))

#
# def func4(l): return l[:2]
# l = [1,2,3]
# print(func4(l))



#
# 5，写函数，计算传入函数的字符串中,[数字]、[字母]、[空格] 以及 [其他]的个数，并返回结果。
def func5(args):
    #s=''
    s1 ={'数字':0,'字母':0,'空格':0,'其他':0}
    for s in args:
        if 65 <= ord(s) <= 122:
            print(s)
            s1['字母'] += 1
        elif s.isdigit():
            s1['数字'] += 1
        elif s.isspace():
            s1['空格'] += 1
        else:
            s1['其他'] += 1
    return s1

#print(func5('12sddsa dwqdw 3232今天下雨'))
# print(ord('a'))
# print(ord('z'))
# print(ord('A'))
# print(ord('Z'))




# 6，写函数，接收两个数字参数，返回比较大的那个数字。
#
# 7，写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# 	dic = {"k1": "v1v1", "k2": [11,22,33,44]}
# 	PS:字典中的value只能是字符串或列表
dic = {"k1": "v1v1", "k2": [11,22,33,44]}
# def func7(argv):
#     dic = {}
#     for i in argv:
#         if len(argv[i]) > 2:
#             dic[i] = argv[i][0:2]
#         else:
#             dic[i] = argv[i]
#     return dic
# print(func7(dic))

# def func1(argv):
#     dic = {}
#     for i in argv:
#         dic[i] = argv[i][:2]
#     return dic
# print(func1(dic))




# 8，写函数，此函数只接收一个参数且此参数必须是列表数据类型，此函数完成的功能是返回给调用者一个字典，此字典的键值对为此列表的索引及对应的元素。
# 例如传入的列表为：[11,22,33] 返回的字典为 {0:11,1:22,2:33}。

# def func8(l):
#     dic = {}
#     for key,value in enumerate(l):
#         dic[key] = value
#     return dic
# print(func8([1,2,3]))


# 9，写函数，函数接收四个参数分别是：姓名，性别，年龄，学历。用户通过输入这四个内容，然后将这四个内容传入到函数中，此函数接收到这四个内容，将内容追加到一个student_msg文件中。
# def fun9(name,sex,age,xl):
#     with open('student_msg',encoding='utf-8',mode='w') as f:
#         f.write('{0},{1},{2},{3}'.format(name,sex,age,xl))
#
# fun9('张三','男','18','大专')


# 10，对第9题升级：支持用户持续输入，Q或者q退出，性别默认为男，如果遇到女学生，则把性别输入女。
#

# 11，写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作（升级题）。




# 12，写一个函数完成三次登陆功能：(升级题,两天做完)
# (1)	用户的用户名密码从一个文件register中取出。
# (2)	register文件包含多个用户名，密码，用户名密码通过|隔开，每个人的用户名密码占用文件中一行。
# (3)	完成三次验证，三次验证不成功则登录失败，登录失败返回False。
# (4)	登陆成功返回True。
# 13，再写一个函数完成注册功能：(升级题,两天做完)
# (1)	用户输入用户名密码注册。
# (2)	注册时要验证（文件regsiter中）用户名是否存在，如果存在则让其重新输入用户名，如果不存在，则注册成功。
# (3)	注册成功后，将注册成功的用户名，密码写入regsiter文件，并以 | 隔开。
# (4)	注册成功后，返回True,否则返回False。
# 明日默写。
# ①，return的作用。
# ②，传参的几种方法，每个都简单写一个代码。
# 如，实参，按位置传参。
# def func(x,y):
# Pass
# func(‘a’,’b’)
def login(username,password):
    with open('register',encoding='utf-8',mode='r') as f:
        for line in f.readlines():
            myuser,mypass = line.strip().split('|')

            if username == myuser and str(password) == mypass:
                print('登录成功')
                return True
            else:
                return False
print()



def func1():
    uname, passwd = input('请输入用户名密码').replace('，', ',').strip().split(',')
    count = 0
    while 1:
        isLogin = int(login(uname, passwd))
        if isLogin == 1:
            break
        else:
            count += 1
        if count == 3:
            print('登录失败')
            return
        uname, passwd = input('请输入用户名密码').replace('，', ',').strip().split(',')
#func1()

def register(username,passwd):
    with open('register',encoding='utf-8',mode='r+') as f:
        for line in f.readlines():
            if username in line:
                print('用户名已经存在')
                return False
        f.write('\n{uname}|{passwd}'.format(uname=username,passwd=passwd))
        return True

print(register('张三1',123))
