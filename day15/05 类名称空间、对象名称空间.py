# author:xuxk
# contact: 徐小康
# datetime:2021/3/24 14:42
# software: PyCharm

"""
文件说明：
"""
# 公共模板
class GameRole:
    rule = '游戏规则'

    def __init__(self,area,nickname,hp,ad):
        self.area = area
        self.nickname = nickname
        self.hp = hp
        self.ad = ad

    def attack(self):
        print('谁施展了一个攻击')


gailun = GameRole('德玛西亚','草丛伦',1000,75)
yasuo = GameRole('艾欧尼亚','托儿所',500,150)
# 1对象为什么能调用类中的属性和方法？
'''
obj.属性名，先从自己空间去找，没有此属性，会通过类对象指针从类去找，类也没有，会从父类去找
'''
gailun.attack = 666
print(gailun.attack)
gailun.rule = gailun.rule # 游戏规则
print(gailun.rule)
# 对象只能查看类中的属性，不能增删改类仲的属性.

# 2.类能不能调用对象的属性？ 不能
# print(GameRole.area)
# 3.对象与对象之间可不可以互相调用?

