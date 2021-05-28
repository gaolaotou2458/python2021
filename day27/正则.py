# author:xuxk
# contact: 徐小康
# datetime:2021/4/27 9:21
# software: PyCharm

"""
文件说明：
"""
import re
# findall
ret = re.findall('\d+','ab22cbd33bde44')
print(ret)



# search
'''
返回一个对象
    通过group去取值
    且只包含第一个匹配到的值
'''

ret = re.search('\d+','ab22cbd33bde44')

print(ret.group())
print(ret.group())

print(2*3)