'''
    中国工商银行账户管理系统：
        ICBC:
'''
import random
import pymysql

# 1.连接数据库
con = pymysql.connect(host="localhost", user="root", password="", database="bank")
# 2.创建控制台
cursor = con.cursor()
bank_name = "中国工商银行昌平回龙观支行"  # 银行名称写死的


class bank:
    def bank_addUser(self, account, username, password, country, province, street, gate, money):
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
        param = [account, username, password, country, province, street, gate, money, bank_name]
        cursor.execute(sql1, param)
        con.commit()  # 提交
        return 1

    # 银行的存款逻辑
    def bank_saveMoney(self, account1, savemoney1):
        a = [account1]
        sql = "select money from user where account = %s"
        cursor.execute(sql, a)
        money1 = cursor.fetchall()

        sql1 = "update user set money = money + %s where account = %s"
        b = [savemoney1, account1]
        cursor.execute(sql1, b)

        con.commit()

        sql2 = "select money from user where account = %s"
        c = [account1]
        cursor.execute(sql2, c)
        money2 = cursor.fetchall()
        if money1 != money2:
            print("存钱成功，账户余额为：", money2[0][0])
            return True
        else:
            return False

    # 银行取钱
    def bank_drawMoney(self, account, password, draw):
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
                c = [account, password]
                cursor.execute(sql3, c)
                money3 = cursor.fetchall()
                if money3[0][0] >= draw:
                    sql1 = "update user set money = money - %s where account = %s and password = %s"
                    b = [draw, account, password]
                    cursor.execute(sql1, b)
                    con.commit()
                    print("取款成功，账户余额为：", money3[0][0] - draw)
                else:
                    return 3
            else:
                return 2
        else:
            return 1

    # 银行的转账逻辑
    def bank_transfer(self, account, password, transfer_account, transfer_money):
        sql = "select account from user where account = %s "
        a = [account]
        cursor.execute(sql, a)
        money1 = cursor.fetchall()
        sql6 = "select account from user where account = %s "
        e = [transfer_account]
        cursor.execute(sql6, e)
        money6 = cursor.fetchall()
        if money1[0][0] == account and money6[0][0] == transfer_account:
            sql1 = "select password,money from user where account = %s "
            b = [account]
            cursor.execute(sql1, b)
            money2 = cursor.fetchall()
            if password == money2[0][0]:
                if money2[0][1] >= transfer_account:
                    sql3 = "update user set money = money - %s where account = %s and password = %s"
                    c = [transfer_account, account, password]
                    cursor.execute(sql3, c)
                    sql4 = "update user set money = money + %s where account = %s"
                    d = [transfer_money, transfer_account]
                    cursor.execute(sql4, d)
                    con.commit()
                    print("转账成功，账户余额为：", money2[0][1] - transfer_money)
                    return 0
                else:
                    return 3
            else:
                return 2
        else:
            return 1

    # 银行的查询账户操作
    def bank_query(self, account, password):
        sql2 = "select * from user where account = %s and password = %s"
        c = [account, password]
        cursor.execute(sql2, c)
        money2 = cursor.fetchall()
        if money2[0][0] == account:
            if money2[0][2] == password:
                return [3, money2]
            else:
                return [2]
        else:
            return [1]
