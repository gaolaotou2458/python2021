# re模块
    # findall search
    # finditer compile
    # 分组命名  (?P<组名>正则表达式)
    # 引用分组命名 (?P=组名)

# 异常处理
    # try/except/else/finally

# 实现能计算类似 带空格 小括号 加减乘除
'1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
# 等类似公式的计算器程序

# 先把所有的空格去掉

# 先计算括号里的，用正则表达式匹配出最内层的小括号
# 先计算乘除
# 再计算加减法
# 得到一个结果
# 将这个结果替换回大表达式

# 再按照上面的过程去计算其他的表达式

# 用上正则
# 50行
# 30行
