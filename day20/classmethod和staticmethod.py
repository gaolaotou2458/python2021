# author:xuxk
# contact: 徐小康
# datetime:2021/3/30 9:13
# software: PyCharm

"""
文件说明：

cls:类名
classmethod:被装饰的类变成一个类方法
类方法的特点：
    只使用类中的资源
        静态属性
        类方法
        property 方法
"""
class Goods:
    __discount = 0.8 #静态属性

    def __init__(self,price):
        self.__price = price #对象属性
        self.name = 'apple'

    @property
    def price(self):
        return self.__price * Goods.__discount

    @classmethod
    def change_discount(cls,new):
        print(cls)
        cls.__discount = new

apple = Goods(10)
banana = Goods(20)

# apple.change_discount(0.7)
Goods.change_discount(0.7)
print(apple.price)
print(banana.price)



print(Goods.__dict__)