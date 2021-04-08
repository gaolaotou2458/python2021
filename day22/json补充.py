# author:xuxk
# contact: 徐小康
# datetime:2021/4/7 10:23
# software: PyCharm

"""
文件说明：
    可以在所有语言中通用
    能够处理的数据非常有限
        在网络操作中，以及多语言环境中，要传递字典、数字、字符串、列表等简单的数据类型的时候使用
    json的字典有非常苛刻的要求：key必须是字符串，且所有字符串必须用“”表示
    dumps(dic/list)     dic/list -->str 序列化方法
    loads(str)          str --> dic/list 反序列方法
    dump(dic/list,f)    dic/list --> 文件 序列化方法
    load(f)             文件 -> dic/list 反序列化方法，多次dump进入文件load的时候报错

"""
import json

# dic = {'name':'喝喝','sex':'male'}
#
# str_dir1 = json.dumps(dic,ensure_ascii=False)
# str_dir2 = json.dumps(dic)
# print(str_dir1)
# print(str_dir2)
#
# with open('json_file',mode='w',encoding='utf-8') as f:
#     f.write(str_dir1)

#

## 方法
# dic = {'name':'喝喝','sex':'male'}
# with open('json_file',mode='w',encoding='utf-8') as f:
#     json.dump(dic,f)

# with open('json_file',mode='r',encoding='utf-8') as f:
#     dic = json.load(f)
#
# print(dic)

## 能不能多次向一个文件中dump,但是不能多次load
# dic = {'name':'喝喝','sex':'male'}
# with open('json_file',mode='w',encoding='utf-8') as f:
#     json.dump(dic,f,ensure_ascii=False)
#     json.dump(dic, f, ensure_ascii=False)
#     json.dump(dic, f, ensure_ascii=False)
#     json.dump(dic, f, ensure_ascii=False)
#     json.dump(dic, f, ensure_ascii=False)

## 需求向文件中写入多个字典！！！

# def my_dumps(dic):
#     with open('json_file', mode='a', encoding='utf-8') as f:
#         dic_str = json.dumps(dic)
#         f.write(dic_str + '\n')
#
# dic1 = {'name':'喝喝','sex':'male'}
# dic2 = {'name':'哈哈','sex':'male'}
# dic3 = {'name':'嘿嘿','sex':'male'}
# my_dumps(dic1)
# my_dumps(dic2)
# my_dumps(dic3)

# with open('json_file',mode='r',encoding='utf-8') as f:
#     for line in f:
#         dic = json.loads(line.strip())
#         print(dic)


data = {'usernmae':['李华','二愣子',],'sex':'mail','age':16}
json_dic2 = json.dumps(data,sort_keys=True,indent=4,separators=(',',':'),ensure_ascii=False)
print(json_dic2)
