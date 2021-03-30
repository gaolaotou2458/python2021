# author:xuxk
# contact: 徐小康
# datetime:2021/3/26 8:58
# software: PyCharm

"""
文件说明：
"""
class Animal:
    def __init__(self,name,kind,food,language):
        #print('初始化')
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


cat = Cat('阿猫','猫科动物','鱼','喵星语')
cat.yell()

dog = Dog('阿狗','小狗','骨头','旺旺语')
dog.look_after_house()
