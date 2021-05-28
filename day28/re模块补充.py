# author:xuxk
# contact: 徐小康
# datetime:2021/4/28 9:06
# software: PyCharm

"""
文件说明：re 上下的方法
学习一个新的规则
"""
import re
# findall

'''search *****'''
# ret = re.match('^\d+','2121wawdadwadw2121')
# print(ret)
# print(ret.group())


'''match
从头开始匹配
'''
# ret = re.match('\d+','2121wawdadwadw2121')
# print(ret)

'''切割split'''
# s1 = 'alex121egon231boss_jin'
# ret = re.split('\d+',s1)
# print(ret)
#
# ret = re.split('(\d+)',s1)
# print(ret)
#
# #给谁加分组就保留谁
# ret = re.split('\d(\d+)',s1)
# print(ret)

'''替换sub'''
s = 'alex121egon231boss_jin'
# ret = re.sub('\d+','|',s)
# print(ret)
# ret = re.sub('\d+','|',s,1)
# print(ret)
'''替换subn'''
# ret = re.subn('\d+','|',s)
# print(ret) #返回替换后的元祖，第二个参数是替换了几次


'''finditer'''
# ret = re.finditer('\d+','abc1cde2fgh3skhfk')
# print(ret)
# for i in ret:
#     print(i.group())

'''compile ****半 编译正则规则
节省时间和空间
'''
# regx = re.compile('\d+')
# ret = regx.search('abc1cde2fgh3skhfk')
# print(ret.group())
# ret = regx.findall('23233')
# print(ret)
#
# ret = regx.finditer('abc1cde2fgh3skhfk')
# for i in ret:
#     print(i.group())

'''分组命名、分组约束
<h1>函数</h1>
'''
# pattern = '<(?P<tag>.*?)>.*?</(?P=tag)>'
# ret =re.search(pattern,'<h1>函数</h1>')
# print(ret)
# if ret:
#     print(ret.group())
#     print(ret.group(1))
#     print(ret.group('tag'))


## 复用第一个分组
pattern = r'<(.*?)>.*?</\1>'
ret =re.search(pattern,'<h1>函数</h1>')
print(ret)
if ret:
    print(ret.group())
    print(ret.group(1))
