# author:xuxk
# contact: 徐小康
# datetime:2021/2/25 13:59
# software: PyCharm

"""
文件说明：
"""

# 读
'''
r 
rb
r+
r+b
'''
# r
def func1():
    f = open('d:\护士主妇空姐私密联系方式.txt',encoding='utf-8',mode='r')
    content = f.read()
    print(content)
    f.close()

def func2():
    f = open('源码/文件操作1',encoding='utf-8',mode='r')
    content = f.read() #读取全部
    print(content)
    f.close()

def func3():
    f = open('源码/文件操作1',encoding='utf-8',mode='r')
    content = f.readline() #按行读取
    print(content)
    f.close()

# 按行读取，翻一个list
def func4():
    f = open('源码/文件操作1',encoding='utf-8',mode='r')
    content = f.readlines() #按行读取
    print(content)
    f.close()

# read(n)
def func5():
    f = open('源码/文件操作1',encoding='utf-8',mode='r')
    content = f.read(6)
    print(content)
    f.close()

# for 循环
def func6():
    f = open('源码/文件操作1',encoding='utf-8',mode='r')
    for line in f:
        print(line.strip())
    f.close()

#func4()
#func5()
#func6()
#rb
# def func_rb():
#     f = open('源码/美女1.jpg',mode='rb')
#     content = f.read()
#     print(content)
#     f.close()
# func_rb()


# 写
# 没有文件，创建文件也要写
# 有文件，先清空后写入
#w
def wirte1():
    f=open('文件操作2',encoding='utf-8',mode='w')
    f.write('测试测试测试')
    f.close()
#wirte1()

'''wb 默认Byte不需要指定编码'''
def wirte2():
    #读图片
    f=open('源码/美女1.jpg',mode='rb')
    content = f.read()
    print(content)
    #写图片
    f1 = open('美女2.jpg',mode='wb')
    f1.write(content)
    f.close()
    f1.close()
#wirte2()

'''追加'''
'''a
# 没有文件，创建文件也要写
# 有文件，直接在文件的最后面追加
'''
def wirte_a():
    f=open('文件操作2',encoding='utf-8',mode='a')
    f.write('\n第3次')
    f.close()
wirte_a()


# 追加


