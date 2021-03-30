# author:xuxk
# contact: 徐小康
# datetime:2021/3/26 8:58
# software: PyCharm

"""
文件说明：
"""
class Animal:

    def __init__(self,name,kind,food,language):
        print('父类初始化')
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
    def __init__(self,name,kind,food,language,eye_color,):
        print('猫咪初始化')
        self.eye_color = eye_color
        Animal.__init__(self, name, kind, food, language)

    def catch_mouse(self):
        print('抓老鼠')

    def eat(self):
        super().eat()
        self.weight = 10
#
class Dog(Animal):
    def look_after_house(self):
        print('看家')

    def eat(self):
        super().eat()
        self.drink()


cat = Cat('阿猫','猫科动物','鱼','喵星语','蓝色')
cat.eat()
print(cat.weight)

dog = Dog('阿狗','小狗','骨头','旺旺语')
dog.eat()
