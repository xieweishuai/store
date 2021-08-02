
class Oldphone():
    __brand = ""  #品牌

    def setbrand(self,brand):
        self.__brand=brand

    def getbrand(self):
        return self.__brand

    def call(self,name):
        print("正在给",name,"打电话...")

class NewPhone(Oldphone):

    def call(self,name):
        print("语音拨号中...")
        super().call(name)

    def introducebrand(self):
        print("品牌为：",self.getbrand(),"的手机很好用...")

phone = NewPhone()
phone.setbrand("华为")
phone.introducebrand()
phone.call("纪博文")

class cookfather():
    __name=""  #姓名
    __age=0   #年龄


    def setname(self,name):
        self.__name=name
    def getname(self):
        return self.__name

    def setage(self, age):
        self.__age = age
    def getage(self):
        return self.__age


    def steamedrice(self):
        print("可以蒸饭")

class cookson(cookfather):
    def stirfry(self):
        print("可以炒菜")


class cookgrandson(cookson):
    def steamedrice(self):
        print("蒸饭")
    def stirfry(self):
        print("炒菜")

cook = cookgrandson()
cook.setname("小明")
cook.setage(18)
print(cook.getname(),cook.getage())
cook.stirfry()
cook.steamedrice()



class person():
    __name = ""  #姓名
    __age = 0    #年龄

    def setname(self, name):
        self.__name = name

    def getname(self):
        return self.__name

    def setage(self, age):
        self.__age = age

    def getage(self):
        return self.__age

class worker(person):
    __sex=""  #性别

    def setsex(self, sex):
        self.__sex = sex

    def getsex(self):
        return self.__sex

    def behavior(self):
        print("干活")

class student(person):
    __sex = "" #性别
    __id = 0  # 学号
    def setsex(self, sex):
        self.__sex = sex

    def getsex(self):
        return self.__sex

    def setid(self,id):
        self.__id=id
    def getid(self):
        return self.__id


    def study(self):
        print("学习")

    def sing(self):
        print("唱歌")
