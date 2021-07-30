#水杯
class  Watercup:
    __height = 0  #水杯高度
    __volume = 0   #水杯容积
    __color = ""   #颜色
    __quality = ""   #材质



    def Setheight(self,height):
        self.__height = height

    def Setvolume(self,volume):
        self.__volume = volume

    def Setcolor(self,color):
        self.__color = color

    def Setquality(self,quality):
        self.__quality = quality

    def Getheight(self):
        return self.__height


    def Storeliquid(self):
        print("能存放液体")



w = Watercup()
w.Setcolor("blue")
w.Setheight(23)
w.Storeliquid()
w.Setheight(10)
w.Getheight()
print(w.Getheight())

#电脑
class computer:
    __ping = 0  #屏幕大小
    __price = 0  #价格
    __cpu = ""   #CPU型号
    __memory = 0  #内存大小
    __standbytime = 0  #待机时长

    def setping(self,ping):
        self.__ping = ping

    def setprice(self,price):
        self.__price = price

    def setcpu(self,cpu):
        self.__cpu = cpu

    def setmempry(self,memory):
        self.__memory = memory

    def setstandbytime(self,standime):
        self.__standbytime = standime

    def computerprint(self):
        print("打游戏")

    def computervideo(self):
        print("看视频")

    def computerplaygame(self):
        print("打游戏")


p = computer()
p.computerplaygame()
p.computerprint()
p.computervideo()


