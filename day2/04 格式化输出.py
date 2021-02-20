# 制作一个模板，某些位置的参数是动态的
# -》字符串动态替换

name = input('请输入姓名:')
age = int(input('请输入年龄:'))
sex = input('请输入性别:')
# % 占位符  s数据类型为字符串 d 数字
# 第一种方式
# msg = '你的名字是%s,年龄%d,你的性别%s' % (name,age,sex)
# print(msg)

# 第2种方式
# msg = '你的名字是%(name1)s,年龄%(age1)d,你的性别%(sex1)s' % {'name1':name,'age1':age,"sex1":sex}
# print(msg)

# bug点 在格式化输出中，只想单纯的表示一个%时，应该用%% 表示，用来转义
msg = '我叫%s,今年%d,我的学习进度1%%' %('小A',23)
print(msg)