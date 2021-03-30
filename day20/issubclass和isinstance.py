# author:xuxk
# contact: 徐小康
# datetime:2021/3/30 9:08
# software: PyCharm

"""
文件说明：
type:只能判断直接类型
isinstance 能判断继承关系
"""


class A: pass
class B(A): pass
a = A()
b = B()
print(type(a))
print(type(b))
print(isinstance(a, A))
print(isinstance(b, A))

print(issubclass(B,A))
print(issubclass(A,B))