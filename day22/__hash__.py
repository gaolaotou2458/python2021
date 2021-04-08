# author:xuxk
# contact: 徐小康
# datetime:2021/4/6 14:56
# software: PyCharm

"""
文件说明：
"""
class Foo():
    pass

obj1 = Foo()
obj2 = Foo()
print(hash(obj1))  #88390632611
print(hash(obj1))  #88390632611
print(hash(obj1))  #88390632611
print(hash(obj1))

# 1.每次执行hash值都会变化
# 2.在一次执行的过程中对同一个值得hash结果总是不变的
# 字典为什么寻址快
dic = {'name':'alex','age':83,'sex':'不详'}
# 字典在内存中是如何存储的？
# 为什么字典的key必须可hash