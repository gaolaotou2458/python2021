# author:xuxk
# contact: 徐小康
# datetime:2021/3/30 9:13
# software: PyCharm

'''
文件说明：

cls:类名
classmethod:被装饰的类变成一个类方法
类方法的特点：
    只使用类中的资源
        静态属性
        类方法
        property 方法
'''
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
#
# apple = Goods(10)
# banana = Goods(20)
#
# apple.change_discount(0.7)
# Goods.change_discount(0.7)
# print(apple.price)
# print(banana.price)
# print(Goods.__dict__)


'''
@staticmethod:静态方法
'''
class Student:
    @staticmethod
    def login(usr,pwd):
        print('@staticmethod',usr,pwd)

Student.login('user','pwd')

'''
类：               调用者
    静态属性        类    所有的对象都统一拥有的属性                                      
    类方法          类    如果这个方法涉及到操作静态属性，类方法、静态方法                       cls表示类
    静态方法        类    普通方法，不使用类中的命名空间，也不使用对象的命名空间 ： 一个普通的函数    没有默认参数
    
    方法           对象                                                                  self表示对象
    property方法   对象                                                                  self表示对象
'''

