from threading import Thread
import time
'''
    厨师：0.5秒制作一个面包，3个厨师同时制作面包，当篮子的面包满了，厨师会等待0.5秒。
    顾客：每个人3000元，同时去买面包，当面包不够时，顾客需要等待一秒。
    篮子：最多容纳600个面包，每个2元。
    一共有六个顾客去抢面包。
'''
basket = 0  # 面包篮子
class Cook(Thread): # 厨师
    def run(self) -> None:
        global basket
        while True:
            time.sleep(0.5)
            basket = basket + 1
            if basket == 600:
                time.sleep(0.5)
class Customer(Thread): # 顾客
    def run(self) -> None:
        username = ""


        global basket
        money = 3000
        while True:
            if basket > 0:
                money = money - 2
                basket = basket - 1
                print(self.username,"买了一个面包")
            else:
                time.sleep(1)
            if money == 0:
                print("没钱了")
                break


c1 = Cook()
c2 = Cook()
c3 = Cook()

Cus1 = Customer()
Cus2 = Customer()
Cus3 = Customer()
Cus4 = Customer()
Cus5 = Customer()
Cus6 = Customer()

Cus1.username="小明"
Cus2.username="小红"
Cus3.username="张三"
Cus4.username="李四"
Cus5.username="王五"
Cus6.username="王六"

c1.start()
c2.start()
c3.start()


Cus1.start()
Cus2.start()
Cus3.start()
Cus4.start()
Cus5.start()
Cus6.start()