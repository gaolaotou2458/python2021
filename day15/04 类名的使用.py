# author:xuxk
# contact: 徐小康
# datetime:2021/3/24 10:21
# software: PyCharm

"""
文件说明：
"""
# class Person:
#     animal = '高级动物'
#     walk_way = '直立行走'
#     language = '语言'
#
#     def eat(self):
#         print('该吃吃,该喝喝')
#
#     def work(self):
#         print('人类都需要工作。。。')

# 类名
# 1查看类中的所有属性和方法
# print(Person.__dict__)
# print(Person.__dict__['animal'])  # 单独的属性及方法可以查，但是不能增删改变
#Person.__dict__['animal'] = '低级动物'
#print(Person.__dict__['animal'])


# 2查看类中的某个，某些属性，某个方法,用万能的 .
# print(Person.animal) # 查
# print(Person.language)
# Person.name = 'alex' # 增
# Person.animal = '低级动物' #改
# del Person.name #删除
# print(Person.name)


# 操作方法,方法一般不通过类名操作
#Person.__dict__['work'](1) 不建议通过这个形式执行方法
#Person.work(666)


# 对象
class Person:
    animal = '高级动物'
    walk_way = '直立行走'
    language = '语言'
    def __init__(self,name,age,eye,language1):  ## 功能：给对象封装属性的。
        self.name1 = name
        self.age = age
        self.eye = eye
        self.language = language1

    def eat(self):
        print('该吃吃,该喝喝')

    def work(self):
        print('人类都需要工作。。。')

#Person() #自动触发 init,这个过程是一个实例化过程，他会实例化一个对象（在内存实例化一个对象空间）
'''
三个阶段
    1.在内存中开辟一个对象空间
    2.自动执行类中的__init__ 方法，并且将对象空间传给self参数。
    3.执行__init__方法，给对象空间封装相应的属性，其他参数手动传入
'''
# person = Person()
# print(person)
# person.work()

person = Person('张三',11,'小眼睛','中文')
# print(person.name1,person.age,person.eye,person.language)
# #查
# print(person.__dict__)
# #增
# person.sex= '男'
# #删除
# del person.eye
# #改
# person.sex = '女'
# print(person.__dict__)

#对象操作类空间的属性，只能查
print(person.animal)
person.animal = '低级动物'
print(person.animal)



