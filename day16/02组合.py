# 3,模拟英雄联盟写一个游戏人物的类（升级题）.
#   要求:
#   (1)创建一个 Game_role的类.
#   (2) 构造方法中给对象封装name,ad(攻击力),hp(血量).三个属性.
#   (3) 创建一个attack方法,此方法是实例化两个对象,互相攻击的功能:
#       例: 实例化一个对象 盖伦,ad为10, hp为100
#       实例化另个一个对象 剑豪 ad为20, hp为80
#       盖伦通过attack方法攻击剑豪,此方法要完成 '谁攻击谁,谁掉了多少血,  还剩多少血'的提示功能.

# 组合： 给一个类的对象封装一个属性，这个属性是另一个类的对象。

class GameRole:
    def __init__(self,name,ad,hp):
        self.name = name
        self.ad = ad
        self.hp = hp

    def attack(self,role):
        role.hp = role.hp -self.ad
        print('{0}攻击{1},{1}掉了{2}血,还剩{3}血'.format(self.name,role.name,self.ad,role.hp))

    def fight(self,role):
        role.hp = role.hp - self.ad - self.weapon.ad
        self.ad = self.ad + self.weapon.ad
        print('{0} 用 {1} 攻击 {2} ,{2} 掉了 {3} 血,还剩 {4} 血'.format(self.name, self.weapon.name, role.name, self.ad, role.hp))

    def equipWeapon(self,weapon):
        self.weapon = weapon



class Weapon:
    def __init__(self,name,ad):
        self.name = name
        self.ad = ad

    def fight(self,role1,role2):
        role2.hp = role2.hp - self.ad
        print('{0} 用 {1} 攻击 {2} ,{2} 掉了 {3} 血,还剩 {4} 血'.format(role1.name,self.name,role2.name,self.ad,role2.hp))

p1 = GameRole('盖伦',20,500)
p2 = GameRole('剑豪',100,200)
# p1.attack(p2)
# print(p2.hp)

w1 = Weapon('大宝剑',30)
w2 = Weapon('武士刀',50)
p1.equipWeapon(w1)
p2.equipWeapon(w2)
p1.fight(p2)
p2.fight(p1)




