import random
# 1. 让系统产生一个随机数
money = 2000  #金币数

while True:
   if money < 200:
      print("对不起你的金币余额不足")
      break
   else:
      data = random.randint(0, 10)
      money = money - 200
      num = input("请输入您要猜的数字：")  # "22"   "23"
      num = int(num)  # "22"  -->  22
      if num > data:
         print("大了！")
         print("金币余额为：", money, "金币！")
      elif num < data:
         print("小了！")
         print("金币余额为：", money, "金币！")
      else:
         money = money + 5000
         print("恭喜，猜中了！本次幸运数字为：", data, "，您获得5000金币奖励，金币余额为：", money, "金币！")
         sun = input("是否继续游戏？1.是  2.否")
         sun = int(sun)
         if sun == 2:
            break
