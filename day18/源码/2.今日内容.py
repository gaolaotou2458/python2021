# -*- coding: utf-8 -*-
# @Time    : 2018/8/28 8:33
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 2.今日内容.py
# @Software: PyCharm

# 面向对象的三大特性
    # 继承
        # 继承和抽象 两个概念
        # 单继承
            # 语法 ： 父类 子类
            # 继承与重用
                # 子类可以使用父类中的名字（变量和方法）
            # 继承与派生
                # 子类在父类的基础上又新创建了自己需要的方法和属性
            # 父类有的子类没有 - 子类对象直接调用 就会直接执行父类的方法
            # 父类有的子类也有 - 子类对象调用 直接执行子类中的方法
            #                   想在子类中使用父类的名字 ： 父类名、super()去调用
            # 规范的编程模式
                # 抽象类
        # 多继承
            # 语法
            # 接口
            # 新式类和经典类
                # 新式类中
                    # 所有的多继承关系寻找方法的顺序  -  遵循广度优先算法
                    # 继承object
                    # mro方法
                    # super : super不是单纯的找父类，而是遵循mro顺序的

                # 经典类
                    # python2.x
                    # 不主动继承object
                    # 经典类在找父类中方法的过程中 遵循 —— 深度优先
                    # 不提供mro方法和super

    # 多态
    # 封装
# c
# c++ c# java python
