import pymysql

# 1.连接数据库
con = pymysql.connect(host="localhost", user="root", password="", database="bank")
# 2.创建控制台
cursor = con.cursor()
account1= 4894894
savemoney1 = 100
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

else:
    pass