# author:xuxk
# contact: 徐小康
# datetime:2021/2/25 8:43
# software: PyCharm

'''
文件说明：
    set:{'wusir','alex',123}
    集合要求里面的元素必须是不可变的数据类型，但是集合本身是可变的数据类型
    集合里面的元素不可重复（天然去重），无序
    主要用途：
        1.去重
        2.关系测试
'''


'''集合的创建'''
# set1= {'alex','wusir'}
# set2=set({'alex','wusir'})
# print(set1)
# print(set2)

'''面试必考：list去重'''
# l1 = [1,1,2,2,3,3,4,5,6,7]
# set1 =set(l1);
# s2 = list(set1)
# print(s2)

# '''新增'''
# set1 = {'alex','wusir','ritian','egon','barry'}
# set1.add('女神')
# '''更新'''
# set1.update('女神1')
#
# '''删除'''
# set1.remove('女神')
# set1.pop() #随机删除
#
# set1.clear()#清空
#
# del set1 #删除集合
#
# print(set1)