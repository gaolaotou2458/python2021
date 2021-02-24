# author:xuxk
# contact: 徐小康
# datetime:2021/2/22 15:28
# software: PyCharm

"""
文件说明：
"""
# 列表，python基础数据类型之一：其他语言中也有列表的概念，js数组
# 可切片，可加步长
# li = ['alex', 123, True, [1, 2, 3], {'name': '太白'}, (222, 33)]

# 第一个 索引，切片，切片+步长
li = ['alex', 123, True, [1, 2, 3], {'name': '太白'}, (222, 33)]
# print(li[0],type(li[0]))
# print(li[1],type(li[1]))
# print(li[:4])
# print(li[::2])
# print(li[-1:-4:-2])
# print(li[-1:2:-2])
l1 = ['alex', 'wusir', 'taibai', '静女神', '文洲', '日天']
# 第二:增删改查，其他方法
# 增
# append 追加到最后
# l1.append('11')
# print(l1)
# name_list = ['张三','李四']
# while 1:
#     username = input('请输入新员工姓名:'.strip())
#     if username.upper() == 'Q' : break
#     name_list.append(username)
# print(name_list)

'''insert(index,元素)插入'''

'''extend(iterable) 迭代追加'''
# l1.extend('abc')
# l1.extend([111,222,333])
# l1.extend(['alex', 'sb'])
# print(l1)

'''删除'''

# 按照索引删除 pop
# print(l1.pop(0)) # 返回值
# print(l1)
'''--按照元素删除'''
# l1.remove('alex')
# print(l1)
'''--清空'''
# l1.clear()
# print(l1)
'''del'''

# 可以按照索引删除
# del l1[0]
# print(l1)
# 可以按照切片删除（可以加步长）
# del l1[0::2]
# print(l1)
# 可以在内存级别删除整个列表
# del l1
# print(l1)

'''改'''
# 按照索引改
# l1[2] = '男神'
# l1[-1]='泰迪'
# print(l1)
# 按照切片（加步长）
# l1[:2] = ['1','2','3']
# print(l1)
# l1[:4] = [1,2,3,4,5,6,7]
# print(l1)
# print(l1)
# l1[:3:2] ='AS'
# print(l1)

'''查'''
print(l1)
# 索引，切片，切片+步长
# for 循环
# for i in l1:
#     print(i)

# 其他方法
# print(len(l1))  # 查询个数
# print(l1.count('日天'))  # 某个元素出现的次数
# index 通过元素找索引
# print(l1.index('wusir'))
#
# l2 = [4,3,1, 2, 3, 4, 5, 6, 7]
# l2.sort() # 从小到大
# l2.sort(reverse=True) #从大到小
# print(l2)

# 第三：列表嵌套。
l3 = ['alex','wusir',['taibai',99,'ritian'],20]
print(l3[0][2])

l3[1] = l3[1].capitalize()
print(l3)

print(l3[2])
l3[2].append('文州')
print(l3)

l3[2][0] = l3[2][0].capitalize()
print(l3)

l3[2][1] = l3[2][1]+1
print(l3)
