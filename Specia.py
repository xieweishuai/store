# 空调
class airconditioner:
    __brand = ""  # 空调品牌
    __price = 0  # 空调价格

    def setbrand(self, brand):
        self.__brand = brand

    def setprice(self, price):
        self.__price = price

    def airtart(self):  # 开机
        print("空调开机了...")

    def airclose(self, hour):  # 定时关机
        print("空调将在", hour, "分钟后自动关闭...")


air = airconditioner()
air.setbrand("格力")
air.setprice(3000)
air.airtart()
air.airclose(199)


# 学生
class Student:
    __username = ""  # 学生姓名
    __age = 0  # 年龄

    def setUsername(self, username):
        self.__username = username

    def getUsername(self):
        return self.__username

    def setAge(self, age):
        if age > 120 or age < 0:
            print("您年龄输入非法！")
        else:
            self.__age = age

    def getAge(self):
        return self.__age

    def showMe(self):
        print("大家好，我叫", self.__username, "，今年", self.__age, "岁了！")

    def compare(self, student):  # self代表我自己    student代表另一个人
        if self.__age > student.getAge():
            print(self.getUsername(), "比", student.getUsername(), "大", (self.__age - student.getAge()), "岁！")
        elif self.__age < student.getAge():
            print(self.getUsername(), "比", student.getUsername(), "小", (student.getAge() - self.__age), "岁！")
        else:
            print("我俩一样大！")


s = Student()
s.setUsername("旺财")
s.setAge(55)
s.showMe()

s1 = Student()
s1.setUsername("李四")
s1.setAge(56)
s1.showMe()

s.compare(s1)  # 旺财要和李四比较
s1.compare(s)


# 人
class person:
    __name = ""  # 姓名
    __sex = ""  # 性别
    __age = 0  # 年龄
    __charge = 30  # 剩余话费
    __brand = ""  # 品牌
    __batterycapacity = 0  # 手机电池容量
    __ping = 0  # 手机屏幕大小
    __hour = 0  # 手机最大待机时长
    __integral = 0  # 所拥有的积分

    def setname(self, name):
        self.__name = name

    def getname(self):
        return self.__name

    def setsex(self, sex):
        self.__sex = sex

    def getsex(self):
        return self.__sex

    def setage(self, age):
        self.__age = age

    def getage(self):
        return self.__age

    def setcharge(self, charge):
        self.__charge = charge

    def getcharge(self):
        return self.__charge

    def setbrand(self, brand):
        self.__brand = brand

    def getbrand(self):
        return self.__brand

    def setbatterycapacity(self, batterycapacity):
        self.__batterycapacity = batterycapacity

    def getbatterycapacity(self):
        return self.__batterycapacity

    def setping(self, ping):
        self.__ping = ping

    def getping(self):
        return self.__ping

    def sethour(self, hour):
        self.__hour = hour

    def gethour(self):
        return self.__hour

    def setintegral(self, integral):
        self.__integral = integral

    def getintegral(self):
        return self.__integral

    def sendmessage(self, person):
        print(self.getname(), "给", person.getname(), "发短信了")

    def phone(self, person, phonetime):
        if person.getname() == "":
            print("此电话为空")
        elif self.getcharge()< 1:
            print("剩余话费不足1元")
        else:
            if phonetime > 0 and phonetime <= 10:
                self.setcharge(self.getcharge() - 1 * phonetime)
                self.setintegral(self.getintegral() + 15 * phonetime)
            elif phonetime > 10 and phonetime <= 20:
                self.setcharge(self.getcharge() - 0.8 * phonetime)
                self.setintegral(self.getintegral() + 39 * phonetime)
            else:
                self.setcharge(self.getcharge() - 0.65 * phonetime)
                self.setintegral(self.getintegral() + 48 * phonetime)


p1 = person()
p1.setname("小明")

print(p1.getcharge())

p2 = person()
p2.setname("小红")
p1.sendmessage(p2)

p1.phone(p2,10)

print(p1.getcharge())


