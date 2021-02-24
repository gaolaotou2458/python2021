# author:xuxk
# contact: 徐小康
# datetime:2021/2/24 10:21
# software: PyCharm

"""
文件说明：
"""
def func1():
    for i in '1234':
        print(i)


#func1();

# 二 id is ==
# name = 'alex'
# print(id(name)) # 在内存中存储的地址
# print(id('alex') == id(name))
# is 是 True == 一定是True 反之则假
# def func2():
#     i1= 1000
#     i2= 1000
#     print(i1 is i2) # 判断两个变量的id值 是否相同
# func2()


'''三小数据池（缓存机制，驻留机制）
python 对内存做的一个优化
将-5 - 256 的整数，以及一定规则的字符串，提前在内存中创建了池
容器里固定放了这些数。
'''
print(id(257) == id(257))
