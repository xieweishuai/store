import random
# 1.准备商品
shop = [
    ["劳力士手表",200000],
    ["Iphone 12X plus",12000],
    ["lenovo PC",6000],
    ["HUA WEI WATCH",1200],
    ["Mac PC",15000],
    ["辣条",2.5],
    ["老干妈",13]
]
# 2. 初始化钱包
money = input("请输入您的余额：")
money = int(money)  # "200000" --> 200000

# 3.空的购物车
mycart = []

#抽优惠卷
sum = input("请问是否抽优惠卷，请输入是或否：")
if sum == "是":
    data = random.randint(0,29)
    data = int(data)

# 4.买东西
i = 0
while i <= 20:
    # 4.1 展示商品
    for key, value in enumerate(shop):
        print(key, value)
    # 4.2 请输入您想要的商品
    chose = input("亲输入您想要的商品编号：") # "1"
    # 4.3
    if chose.isdigit():
        chose = int(chose)
        # 4.4 先判断是否存在该商品
        if chose > 6:
            print("您输入的商品不存在！别瞎弄！")
        else:
            # 4.5 判断您的余额是否足够
            if money < shop[chose][1]:
                print("对不起，穷鬼，您的钱不够！请到其他超市买东西去！")
            else:
                # 4.6 将商品添加到购物车 ，余额减去对应的钱
                mycart.append(shop[chose])
                if data >= 0 and data < 10 and chose == 6:
                    print("恭喜使用老干妈七折优惠卷")
                    money = money - shop[chose][1]*0.7
                    data = 30
                elif data <= 29 and data > 9 and chose == 2:
                    print("恭喜使用联想一折优惠卷卷")
                    money = money - shop[chose][1]*0.1
                    data = 30
                else:
                    money = money - shop[chose][1]
                print("恭喜，成功添加购物车！您的余额还剩￥：",money)
    elif chose == "q" or chose == "Q":
        print("拜拜了，您嘞！欢迎下次光临！")
        break
    else:
        print("对不起，您输入有误，请重新输入！")
    i = i + 1

# 打印购物小条
print("以下是您的购物小条，请拿好：")
for key ,value in  enumerate(mycart):
    print(key,value)
print("本次余额还剩：￥",money)