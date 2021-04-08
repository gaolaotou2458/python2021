# -*- coding: utf-8 -*-
# @Time    : 2018/8/31 10:59
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 5.作业讲解.py
# @Software: PyCharm

# 场景 角色 类 —> 属性和方法
# 站在每个角色的角度上去思考程序执行的流程
import sys
import pickle
class Course:
    def __init__(self,name,price,period,teacher):
        self.name = name
        self.price = price
        self.period = period
        self.teacher = teacher

class Student:
    operate_lst = [
                   ('查看所有课程', 'show_courses'),
                   ('选择课程', 'select_course'),
                   ('查看已选课程', 'check_selected_course'),
                   ('退出', 'exit')]
    def __init__(self,name):
        self.name = name
        self.courses = []

    def show_courses(self):
        print('查看可选课程')

    def select_course(self):
        print('选择课程')

    def check_selected_course(self):
        print('查看已选课程')

    def exit(self):
        exit()

    @classmethod
    def init(cls,name):
        #返回一个学生对象
        #从文件抓取 load
        with open('student_info', 'rb') as f:
            while True:
                try:
                    stu = pickle.load(f)
                    if(stu.name == name):return stu
                except EOFError:
                    break


class Manager:
    operate_lst = [('创建课程','create_course'),
                   ('创建学生','create_student'),
                   ('查看所有课程','show_courses'),
                   ('查看所有学生','show_students'),
                   ('查看所有学生的选课情况','show_student_course'),
                   ('退出','exit')]
    def __init__(self,name):
        self.name = name
        self.courses = []

    def create_course(self):
        name = input('course Name:')
        price = input('course price:')
        period = input('course period:')
        teacher =input('course teacher:')
        course_obj = Course(name,price,period,teacher)
        with open('course_info','ab') as f:
            pickle.dump(course_obj,f)
        print('%s课程创建完毕' %course_obj.name)


    def create_student(self):
        # 用户名和密码记录到course_info
        stu_name = input('用户名:')
        stu_passwd = input('密码:')
        stu_auth = '%s|%s|Student\n'%(stu_name,stu_passwd)
        stu_obj = Student(stu_name)
        #将学生对象存储在student_info文件
        with open('userinfo','a',encoding='utf-8') as f:
            f.write(stu_auth)
        with open('student_info','ab') as f:
            pickle.dump(stu_obj,f)
        print('%s学生创建成功' %stu_obj.name)

    def show_courses(self):
        with open('course_info', 'rb') as f:
            while True:
                try:
                    course = pickle.load(f)
                    print('课程名:%s,课程价格:%s,课程周期:%s,课程老师:%s' %(course.name,course.price,course.period,course.teacher))
                except EOFError:
                    break


    def show_students(self):
        print('查看所有学生')

    def show_student_course(self):
        print('查看所有学生的选课情况')

    def exit(self):
        exit()

    @classmethod
    def init(cls,name):
        return cls(name) #管理员对象

# 学生 ： 登录就可以选课了
    # 有学生账号了
    # 有课程了

# 管理员 ：登录就可以完成以下功能
    # 学生的账号是管理员创建的
    # 课程也应该是管理员创建的

# 应该先站在管理员的角度上来开发
# 登录
# 登录必须能够自动识别身份
# 用户名|密码|身份
def login():
    name = input('username : ')
    pawd = input('password : ')
    with open('userinfo',encoding='utf-8') as f:
        for line in f:
            usr,pwd,identify = line.strip().split('|')
            if usr == name and pawd == pwd:
                return {'result':True,'name':name,'id':identify}
        else:
            return {'result':False,'name':name}

ret = login()
if ret['result']:
    print('登录成功')
    if hasattr(sys.modules[__name__],ret['id']):
        cls = getattr(sys.modules[__name__],ret['id'])
        #obj = cls(ret['name'])  # 实例化
        obj = cls.init(ret['name'])
        print('%s登录成功' %obj.name)
        while True:
            for id,item in enumerate(cls.operate_lst,1):
                print(id,item[0])
            func_str = cls.operate_lst[int(input('>>>')) - 1][1]
            print(func_str)
            if hasattr(obj,func_str):
                getattr(obj,func_str)()
else:
    print('登录失败')

    # if ret['id'] == 'Manager':
    #     obj = Manager(ret['name'])
    #     for id,item in enumerate(Manager.operate_lst,1):
    #         print(id,item[0])
    #     func_str = Manager.operate_lst[int(input('>>>')) - 1][1]
    #     if hasattr(obj,func_str):
    #         getattr(obj,func_str)()
    # elif ret['id'] == 'Student':
    #     obj = Student(ret['name'])
    #     for id,item in enumerate(Student.operate_lst,1):
    #         print(id,item[0])
    #     func_str = Student.operate_lst[int(input('>>>')) - 1][1]
    #     if hasattr(obj,func_str):
    #         getattr(obj,func_str)()