# author:xuxk
# contact: 徐小康
# datetime:2021/3/9 14:00
# software: PyCharm

"""
文件说明：
"""
# i = 0
# def func(i):
#     i+=1
#     print(i)
#     func(i)
#
#
# func(i)
# import sys
# sys.setrecursionlimit(100000)
# i = 0
# def func(i):
#     i+=1
#     print(i)
#     func(i)
#
#
# func(i)


'''
alex  比 wusir 大两岁 n = 4
wusir 比日天 大两岁  n= 3
日天 比太白 大两岁  n = 2
太白 24岁 n = 1
'''


def age(n):
    if(n ==1) :
        return 24
    else:
        return age(n-1) + 2

print(age(4))
