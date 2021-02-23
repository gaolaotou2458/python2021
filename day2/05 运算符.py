# and or not
# 优先级() > not > and > or

print(1 < 2 and 3 > 4 or 8 < 6 and 9 > 5 or 7 > 2)


# 第二种情况
'''
x or y if x is True,return x
'''
#print(1 or 2)
#print(0 or 2)
# 补充
# int ---> bool
# 0-----> False 非0---->True

print(1 or 3 and 5 or 4) #1
print(0 or 3 and 5 or 4) #5

# 变态面试题：
print(1 > 2 or 3 and 4 < 6) # True
print(1 > 2 or 4 < 6)
print(2 or 3 and 4 < 6)  #2

# 应用
# 1 if while 行条件判断
# 2，面试.