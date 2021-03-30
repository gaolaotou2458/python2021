# author:xuxk
# contact: 徐小康
# datetime:2021/3/26 8:55
# software: PyCharm

"""
文件说明：
"""
class Animal:
    def __init__(self,name,kind,food,language):
        self.name = name
        self.kind = kind
        self.food = food
        self.language = language
    def yell(self):
        print('%s叫'%self.language)
    def eat(self):
        print('吃%s'%(self.food))
    def drink(self):
        print('喝水')
#
class Cat(Animal):
    def catch_mouse(self):
        print('抓老鼠')
#
class Dog(Animal):
    def look_after_house(self):
        print('看家')

animal = Animal('老鼠','猫科动物','鱼','喵星语')
cat = Cat('老鼠','猫科动物','鱼','喵星语')
cat.yell()