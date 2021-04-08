# author:xuxk
# contact: 徐小康
# datetime:2021/4/1 9:37
# software: PyCharm

"""
文件说明：
"""
class Course:
    def __init__(self,name,period,price,teacher):
        self.name = name
        self.period = period
        self.price = price
        self.teacher = teacher

    def __str__(self):
        return 'str: %s %s %s %s' % (self.name,self.period,self.price,self.teacher)

    def __repr__(self):
        return '__repr__: %s %s %s %s' % (self.name, self.period, self.price, self.teacher)
course_lst = []

python = Course('Python','6个月',29800,'boos jin')
course_lst.append(python)
linux = Course('linux','5个月',25800,'old boy')
course_lst.append(linux)
for id,course in enumerate(course_lst,1):
    # print(id,course)
    # print('%s %s' %(id,course))
    # print(str(course))
    print(repr(course))
    print('%r' %course)
# 当你打印一个对象的时候 触发__str__
# 当你使用%s格式化的时候 触发__str__
# str强制数据类型的时候  触发__str__

# __repr__
# repr是str的备胎

# 学生选择课程的时候，要显示所有的课程