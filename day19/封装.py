# author:xuxk
# contact: 徐小康
# datetime:2021/3/29 13:18
# software: PyCharm

"""
文件说明：
"""



#print(Goods.__discount) # 在类的外部无法访问私有的静态变量
'''
    类中的静态变量和方法名在程序加载的过程中就已经执行完成了，不需要等待调用
    在这个类加载完成之前，Goods这个名字还没有出现在内存空间中
    私有的静态属性可以在类的内部使用，用来隐藏某个变量的值
'''
# class Goods:
#     __discount = 0  # 私有的静态变量
#     print(__discount)
#     def test1(self):
#         print(self.__discount)
# # good = Goods();
# # good.test1()
# print(Goods.__dict__)
# print(Goods._Goods__discount) # 编程规范的角度上出发 我们不能在类的外部使用私有的变量

class Goods:
    __discount = 0.7    # 私有的静态变量
    def __init__(self,name,price):
        self.name = name
        self.__price = price

    def price(self):
        return self.__price * Goods.__discount

    def change_price(self,new_price):
        if type(new_price) is int:
            self.__price = new_price
        else:
            print('本次价格修改不成功')

apple = Goods('APPLE',5)
print(apple.price())
apple.change_price('aaaa')
print(apple.price())

# class Student:
#     def __init__(self,name):
#         self.__name = name
#
#     def getName(self):
#         return self.__name
# zhuge = Student('诸葛')
# print(zhuge.getName())

class User:
    def __init__(self, username, password):
        self.usr = username
        self.__pwd = password
        self.pwd = self.__getPwd()

    def __getPwd(self):
        return hash(self.__pwd)

    def change_price(self,new_price):
        if type(new_price) is int:
            self.__price = new_price

user = User('alex','alex110')
print(user.usr,user.pwd)
