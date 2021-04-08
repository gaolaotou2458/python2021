# author:xuxk
# contact: 徐小康
# datetime:2021/4/6 14:52
# software: PyCharm

"""
文件说明：
"""
class Staff:
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

alex1 = Staff('alex1','不详')
alex2 = Staff('alex2','不详')
alex3 = Staff('alex2','不详')

print(alex1 == alex2)
print(alex2 == alex3)