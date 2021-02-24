# author:xuxk
# contact: 徐小康
# datetime:2021/2/23 10:26
# software: PyCharm

"""
range: 自定制的  数字泛微的 列表 可迭代对象类比成列表
# range() 一般和for循环结合使用
"""
# s1 = range(1, 101)
# for i in s1:
#     print(i)

# s1 = range(2, 101, 2)
# for i in s1:
#     print(i)

# for i in range(10, 1, -1):
#     print(i)

#计算每个元素的索引
l1 = ['alex', 'alex', 'wusir', 'taibai', '静女神', '文洲', '日天']
## 方法一：不好 重复判断
# for i in l1:
#     print(l1.index(i))

# for i in range(0, len(l1)):
#     print('第{0}个元素{1}:'.format(i,l1[i]))
print('a' in l1)
print('alex' in l1)
print('alex' not in l1)
