# author:xuxk
# contact: 徐小康
# datetime:2021/3/29 13:59
# software: PyCharm

"""
文件说明：
"""
### 私有变量能不能被继承
class A:
    __country = 'China'

class B(A):
    pass
    # print(__country) #NameError: name '_B__country' is not defined