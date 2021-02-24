# author:xuxk
# contact: 徐小康
# datetime:2021/2/23 10:10
# software: PyCharm

"""
文件说明：元祖 只读列表
"""
tul = ('alex', 100, True, [1, 2, 3], {'name': '太白'}, (22, 33))
# 索引，切片，切片+片长
# print(tul[0])
# print(tul[:3])
# index len count
# 应用场景： 一些非常重要的数据，不允许所有人修改，放在元祖中
# 儿子不能改，孙子可以改 alex 不能改，【1，2，3】 里面的内容可以改

tul[3].append(666)
print(tul)



