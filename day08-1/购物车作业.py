# author:xuxk
# contact: 徐小康
# datetime:2021/2/26 8:31
# software: PyCharm

"""
文件说明：
"""
'''
#1.用户先给自已的账户充钱:比如先充3000元。#2.页面显示序号±商品名称+商品价格，如:
1电脑1999
2鼠标10…
n购物车结算
I
3.用户输入选择的商品序号，然后打印商品名称及商品价格,并将此商品，添加到购物车，用户还可
4．如果用户输入的商品序号有误，则提示输入有误，并重新输入。
5．用户输入n为购物车结算，依次显示用户购物车里面的商品，数量及单价，若充值的钱数不足，则
6.用户输入Q或者q退出程序。
7．退出程序之后，依次显示用户购买的商品，数量，单价，以及此次共消费多少钱，账户余额多少。

'''
#1.用户先给自已的账户充钱:比如先充3000元。#2.页面显示序号±商品名称+商品价格，如:

goods = [{"name": "电脑", "price": 1999},
         {"name": "鼠标", "price": 10},
         {"name": "游艇", "price": 20},
         {"name": "美女", "price": 998}]

while 1:
    # 充钱
    money = input('请输入充值数额:').strip()
    if money.isdigit():
        money = int(money)
        break
    else:
        print('包含非数字元素，重新输入')
carDic = {}
while 1:
    for index,good in enumerate(goods) :
        print('序号:{0},商品名称:{1},价格:{2}'.\
              format(index + 1, good['name'], good['price']))
    #break

    selectId = input('请输入商品序号,(输入q 或者 Q退出，输入n 结算)').strip()
    if selectId.isdigit():
        selectId = int(selectId)
        if 0 <  selectId <= len(goods):
            if int(selectId) in carDic:
                #carDic.update({selectId:carDic.get(selectId) + 1})
                carDic[selectId] += 1
            # 更新序号，取不到序号默认给0 再加1
            else:
                carDic[selectId] = carDic.get(int(selectId), 0) + 1
        else:
            print('输入的商品号不存在')
        print(carDic)
    elif selectId.upper() == 'Q':
        break
    elif selectId.upper() == 'N':
        '''计算购物车'''
        total = 0
        lastMoney = 0
        print('您购买的商品如下')
        for index,shop in carDic.items():
            print('商品名称:{1},价格:{2},数量:{0}'.format(shop, goods[index - 1]['name'], goods[index - 1]['price']))
            total += goods[index-1]['price'] * shop
        lastMoney = money - total
        if lastMoney <0: print('金额不足，请继续充值')
        print('总消费{0},剩余{1}'.format(total,lastMoney))
        break
    else:
        print('输入有误')



def test1():
    carDic = {0:2}
    count = carDic.get(0,0)+1
    print()
    if 0 in carDic:
        carDic[0] = carDic.get(0,0)+1
    else:
        carDic.update({0,1})
    #print(carDic)

#test1()