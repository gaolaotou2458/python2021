# 1、匹配整数或者小数（包括正数和负数）
# 2、匹配年月日日期 格式2018-12-31
# 3、匹配qq号 5-12
# 4、11位的电话号码
# 5、长度为8-10位的用户密码 ： 包含数字字母下划线
# 6、匹配验证码：4位数字字母组成的
# 7、匹配邮箱地址 邮箱规则
# 8、从类似
# <a>wahaha</a>
# <b>banana</b>
# <h1>qqxing</h1>
# <h1>q</h1>
# 这样的字符串中，
# 1）匹配出wahaha，banana，qqxing内容。
# 2）匹配出a,b,h1这样的内容

a = '1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'
# 9、1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))
# 1）从上面算式中匹配出最内层小括号以及小括号内的表达式

# 10、从类似9.0-2.22*5/3+7/3*99/4*2998+10*568/14的表达式中匹配出从左到右第一个乘法或除法
