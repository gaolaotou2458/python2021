# author:xuxk
# contact: 徐小康
# datetime:2021/2/24 9:23
# software: PyCharm

"""
文件说明：
集合是无序的，不重复的数据集合，它里面的元素是可哈希的(不可变类型)，但是集合本身是不可哈希（所以集合做不了字典的键）的。以下是集合最重要的两点：
　　去重，把一个列表变成集合，就自动去重了。
　　关系测试，测试两组数据之前的交集、差集、并集等关系。
"""
'''集合的创建'''
# set1 = set({1,2,'barry'})
# set2 = {1,2,'barry'}
# print(set1,set2)  # {1, 2, 'barry'} {1, 2, 'barry'}
'''2，集合的增。'''
set1 = {'alex','wusir','ritian','egon','barry'}
# set1.add('景女神')
# print(set1)

#update：迭代着增加
# set1.update('A')
# print(set1)
# set1.update('老师')
# print(set1)
# set1.update([1,2,3])
# print(set1)
'''3，集合的删。'''
# set1 = {'alex','wusir','ritian','egon','barry'}
#
# set1.remove('alex')  # 删除一个元素
# print(set1)
#
# set1.pop()  # 随机删除一个元素
# print(set1)
#
# set1.clear()  # 清空集合
# print(set1)
#
# del set1  # 删除集合
# print(set1)

'''enumerate：枚举，对于一个可迭代的（iterable）/可遍历的对象（如列表、字符串），enumerate将其组成一个索引序列，利用它可以同时获得索引和值。'''
li = ['alex','银角','女神','egon','太白']
for i in enumerate(li):
    print(i)
for index,name in enumerate(li,1):
    print(index,name)
for index, name in enumerate(li, 100):  # 起始位置默认是0，可更改
    print(index, name)
