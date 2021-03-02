# author:xuxk
# contact: 徐小康
# datetime:2021/2/26 13:02
# software: PyCharm

"""
文件说明：
"""

# def func1(s):
#     count = 0
#     for i in s:
#         count+=1
#     return count
# s = '212'
# print(func1(s))

def my_len(args):
    count = 0
    for i in args:
        count += 1
    return count

print(my_len({1:1,2:2}))