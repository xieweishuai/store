'''
    中国工商银行账户管理系统：
        ICBC:
'''
import random
import pymysql
# 1.连接数据库
con = pymysql.connect(host="localhost",user="root",password="",database="bank")
# 2.创建控制台
cursor = con.cursor()
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
    sql = "select * from user"
    cursor.execute(sql)
    bank = cursor.fetchall()
    # 1.判断数据库是狗已满
    if len(bank) >= 100:
        return 3
    # 2.判断用户是否存在
    if username in bank:
        return 2
    # 3.正常开户
    sql1 = "insert into user values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    param = [account,username,password,country, province, street, gate, money,bank_name]
    cursor.execute(sql1,param)
    con.commit()  # 提交
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
def bank_saveMoney(account1, savemoney1):
    a = [account1]
    sql = "select money from user where account = %s"
    cursor.execute(sql,a)
    money1 = cursor.fetchall()

    sql1 = "update user set money = money + %s where account = %s"
    b = [savemoney1,account1]
    cursor.execute(sql1,b)

    con.commit()

    sql2 = "select money from user where account = %s"
    c = [account1]
    cursor.execute(sql2,c)
    money2 = cursor.fetchall()
    if money1 != money2:
        print("存钱成功，账户余额为：",money2[0][0])
        return True
    else:
        return False


# 用户的存钱操作逻辑
def user_saveMoney():
    while True:
        account1 = input("请输入您的账号：")
        savemoney1 = input("请输入您的存款金额：")
        if account1.isdigit() and savemoney1.isdigit():
            account1 = int(account1)
            savemoney1 = int(savemoney1)
            break
        else:
            print("输入错误，请重新输入")

    status = bank_saveMoney(account1, savemoney1)
    if status == False:
        print("对不起，该账户不存在")

# 银行取钱
def bank_drawMoney(account,password,draw):
    a = [account]
    sql = "select account from user where account = %s"
    cursor.execute(sql, a)
    money1 = cursor.fetchall()
    if account == money1[0][0]:
        sql2 = "select password from user where account = %s"
        cursor.execute(sql2, a)
        money2 = cursor.fetchall()
        if password == money2[0][0]:
            sql3 = "select money from user where account = %s and password = %s"
            c = [account,password]
            cursor.execute(sql3, c)
            money3 = cursor.fetchall()
            if money3[0][0] >= draw:
                sql1 = "update user set money = money - %s where account = %s and password = %s"
                b = [draw,account,password]
                cursor.execute(sql1, b)
                con.commit()
                print("取款成功，账户余额为：",money3[0][0] - draw)
            else:
                return 3
        else:
            return 2
    else:
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
    sql = "select account from user where account = %s "
    a = [account]
    cursor.execute(sql, a)
    money1 = cursor.fetchall()
    sql6 = "select account from user where account = %s "
    e = [transfer_account]
    cursor.execute(sql6, e)
    money6 = cursor.fetchall()
    if  money1[0][0] == account and money6[0][0] == transfer_account:
        sql1 = "select password,money from user where account = %s "
        b = [account]
        cursor.execute(sql1, b)
        money2 = cursor.fetchall()
        if password == money2[0][0]:
            if money2[0][1] >= transfer_account:
                sql3 = "update user set money = money - %s where account = %s and password = %s"
                c = [transfer_account,account,password]
                cursor.execute(sql3, c)
                sql4 = "update user set money = money + %s where account = %s"
                d = [transfer_money,transfer_account]
                cursor.execute(sql4, d)
                con.commit()
                print("转账成功，账户余额为：",money2[0][1] - transfer_money)
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
    sql2 = "select * from user where account = %s and password = %s"
    c = [account,password]
    cursor.execute(sql2, c)
    money2 = cursor.fetchall()
    if money2[0][0] == account:
        if money2[0][2] == password:
            return [3,money2]
        else:
            return [2]
    else:
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
        print(info % (status[1][0][1],status[1][0][0],status[1][0][2],status[1][0][7],status[1][0][3],status[1][0][4],
                      status[1][0][5],status[1][0][6],bank_name))


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
