# author:xuxk
# contact: 徐小康
# datetime:2021/2/24 15:49
# software: PyCharm

"""
文件说明：
"""
#如果b1: gbk的bytes类型，-----> utf-8 的bytes类型怎么办？
# b1 = '太白'.encode('gbk')
# print(b1)
#
# b2 = b1.decode('gbk').encode('utf-8')
# print(b2)
#
# b3 = b2.decode('utf-8')
# print(b3)