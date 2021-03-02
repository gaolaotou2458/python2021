# author:xuxk
# contact: 徐小康
# datetime:2021/2/25 15:12
# software: PyCharm

"""
文件说明：
"""
mylist = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5]
set1 = set(mylist)
dic = {}
dic = dic.fromkeys(set1, 0)
for i in mylist:
    if i in dic: dic[i] += 1
print(dic)
