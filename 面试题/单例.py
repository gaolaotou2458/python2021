# author:xuxk
# contact: 徐小康
# datetime:2021/4/6 14:04
# software: PyCharm

"""
文件说明：
"""
## 单例模式
class Foo:
    __instance =None;
    def __init__(self,name):
        self.name = name
        print('执行了init')

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)  ##开辟空间
        return cls.__instance


obj1 = Foo('alex')
obj2 = Foo('egon')
print(obj1 == obj2)
print(obj1.name,obj2.name)