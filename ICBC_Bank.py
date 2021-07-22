'''
    中国工商银行账户管理系统：
        ICBC:
'''
import random

# 1.准备一个数据库 和 银行名称
bank = {}  # 空的数据库
'''
    {
        "张三":{
            account:s001,
            country:"中国"
        }，
        "李四":{
            
        }
    
    
    }

'''
bank_name = "中国工商银行昌平回龙观支行"  # 银行名称写死的


# 2.入口程序
def welcome():
    print("*************************************")
    print("*      中国工商银行昌平支行           *")
    print("*************************************")
    print("*  1.开户                            *")
    print("*  2.存钱                            *")
    print("*  3.取钱                            *")
    print("*  4.转账                            *")
    print("*  5.查询                            *")
    print("*  6.Bye！                           *")
    print("**************************************")


# 银行的开户逻辑
def bank_addUser(account, username, password, country, province, street, gate, money):
    # 1.判断数据库是狗已满
    if len(bank) >= 100:
        return 3
    # 2.判断用户是否存在
    if username in bank:
        return 2
    # 3.正常开户
    bank[username] = {
        "account": account,
        "password": password,
        "country": country,
        "province": province,
        "street": street,
        "gate": gate,
        "money": money,
        "bank_name": bank_name
    }
    return 1


# 用户的开户的操作逻辑
def addUser():
    username = input("请输入您的用户名：")
    password = input("请输入您的开户密码：")
    country = input("请输入您的国籍：")
    province = input("请输入您的居住省份：")
    street = input("请输入您的街道：")
    gate = input("请输入您的门牌号：")
    money = int(input("请输入您的开户初始余额："))  # 将输入金额转换成int类型
    # 随机产生8为数字
    account = random.randint(10000000, 99999999)

    status = bank_addUser(account, username, password, country, province, street, gate, money)

    if status == 3:
        print("对不起，用户库已满，请携带证件到其他银行办理！")
    elif status == 2:
        print("对不起，该用户已存在！请勿重复开户！")
    elif status == 1:
        print("开户成功！以下是您的个人开户信息：")
        info = '''
            ----------个人信息------
            用户名：%s
            密码：%s
            账号：%s
            地址信息
                国家：%s
                省份：%s
                街道：%s
                门牌号: %s
            余额：%s
            开户行地址：%s
            ------------------------
        '''
        print(info % (username, password, account, country, province, street, gate, money, bank_name))


# 银行的存款逻辑
def bank_saveMoney(account, savemoney1):
    for key in bank:
        #判断是否存在该账号
        if bank[key]["account"] == account:
            #若存在该账号，进行存款操作
            bank[key]["money"] = bank[key]["money"] + savemoney1
            print("存款成功，账户余额为：", bank[key]["money"])
            return True
        else:
            continue
    return False


# 用户的存钱操作逻辑
def user_saveMoney():
    account = int(input("请输入您的账号："))
    savemoney1 = int(input("请输入您的存款金额："))
    status = bank_saveMoney(account, savemoney1)
    if status == False:
        print("对不起，该账户不存在")

# 银行取钱
def bank_drawMoney(account,password,draw):
    i = 0
    for key in bank:
        # 判断是否存在该账号
        if bank[key]["account"] == account:
            i = i + 1
            # 判断是否密码是否正确
            if bank[key]["password"] == password:
                #判断取钱金额是否超过账号
                if bank[key]["money"] >= draw:
                    #进行取钱操作
                    bank[key]["money"] = bank[key]["money"] - draw
                    print("取款成功，账户余额为：", bank[key]["money"])
                    return 0
                else:
                    return 3
            else:
                return 2

    if i == 0:
        return 1

# 用户的取钱操作逻辑
def user_drawMoney():
    account = int(input("请输入您的账号："))
    password = input("请输入您的账户密码：")
    draw = int(input("请输入您的取款金额："))
    status = bank_drawMoney(account,password,draw)
    if status == 1:
        print("账户不存在")
    elif status == 2:
        print("密码不正确")
    elif status == 3:
        print("钱不够")

#银行的转账逻辑
def bank_transfer(account,password,transfer_account,transfer_money):
    i = 0
    j = 0
    for key in bank:
        # 判断是否存在自己账号
        if bank[key]["account"] == account:
            key1 = key
            i = i + 1
        # 判断是否存在转入账号
        if bank[key]["account"] == transfer_account:
            key2 = key
            j = j + 1
    if i == 1 and j == 1:
        #判断自己账号密码是否正确
        if bank[key1]["password"] == password:
            #判断转账金额是否超出账户金额
            if bank[key1]["money"] >= transfer_money:
                #转出操作
                bank[key1]["money"] = bank[key1]["money"] - transfer_money
                #转入操作
                bank[key2]["money"] = bank[key2]["money"] + transfer_money
                print("转账成功，账户余额为：", bank[key1]["money"])
                return 0
            else:
                return 3
        else:
            return 2
    else:
        return 1

# 用户的转账操作逻辑
def user_transfer():
    account = int(input("请输入你的账号："))
    password = input("请输入您的账户密码：")
    transfer_account = int(input("请输入你要转入的账号："))
    transfer_money = int(input("请输入您的转账的金额："))
    status = bank_transfer(account,password,transfer_account,transfer_money)
    if status == 1:
        print("账号不对")
    elif status == 2:
        print("密码不对")
    elif status == 3:
        print("钱不够")


#银行的查询账户操作
def bank_query(account,password):
    i = 0
    for key in bank:
        #判断账户是否存在
        if bank[key]["account"] == account:
            i = i + 1
            #判断密码是否正确
            if bank[key]["password"] == password:
                #返回账户信息
              return [3,key,account,password,bank[key]["money"],bank[key]["country"],bank[key]["province"],
                      bank[key]["street"],bank[key]["gate"],bank[key]["bank_name"]]
            else:
                return [2]

    if i == 0:
        return [1]


# 用户的查询账户功能
def user_query():
    account = int(input("请输入您的账号："))
    password = input("请输入您的账户密码：")
    status = bank_query(account,password)
    if status[0] == 1:
        print("账号不对")
    elif status[0] == 2:
        print("密码不对")
    elif status[0] == 3:
        print("查询成功！以下是您的个人账户信息：")
        info = '''
                    ----------账户信息------
                    用户名：%s
                    当前账号：%s
                    密码：%s
                    余额：%s
                    地址信息
                        国家：%s
                        省份：%s
                        街道：%s
                        门牌号: %s
                    当前账户的开户行地址：%s
                    ------------------------
                '''
        print(info % (status[1],status[2],status[3],status[4],status[5],status[6],status[7],status[8],status[9]))


while True:
    # 打印欢迎程序
    welcome()
    chose = input("请输入您的业务：")
    if chose == "1":
        addUser()
    elif chose == "2":
        user_saveMoney()
    elif chose == "3":
        user_drawMoney()
    elif chose == "4":
        user_transfer()
    elif chose == "5":
        user_query()
    elif chose == "6":
        print("欢迎下次光临！")
        break
    else:
        print("输入错误！请重新输入！")
