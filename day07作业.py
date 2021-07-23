
import xlrd
#选项列表
month = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]
#衣服列表
closh = ["T血","风衣","马甲","牛仔裤","皮草","皮衣","小西装","羽绒服"]
sum = 0
#衣服销售量列表
sale = []
sa = 0
#每月销售总额列表
volume = []
#每季度销售额列表
su = [0,0,0,0]
#每月销售额统计
def monthMoney(m):
    # 1. 打开工作簿
    wd = xlrd.open_workbook(filename="2020年每个月的销售情况.xlsx", encoding_override=True)
    money = 0
    # 月份列表

    # 2.打开您要的选项卡
    st = wd.sheet_by_name(m)
    # 3.读取数据
    rows = st.nrows  # 获取行数  # 4

    for i in range(1,rows):
        data = st.row_values(i)
        money = data[2]*data[4] + money
    return  money

#计算每种衣服的销量
def closhMoney(closh):
    # 1. 打开工作簿
    wd = xlrd.open_workbook(filename="2020年每个月的销售情况.xlsx", encoding_override=True)
    money = 0
    sum = 0
    # 月份列表
    # 2.打开您要的选项卡
    for m in month:
        st = wd.sheet_by_name(m)
        # 3.读取数据
        rows = st.nrows  # 获取行数  # 4
        for i in range(1, rows):
            data = st.row_values(i)
            if closh == data[1]:
                money = data[2] * data[4] + money
                sum = sum +data[4]

    return money,sum

#每月销售总额
for m in month:
    money = monthMoney(m)
    print(m,"的销售总额额为：",money)
    volume.append(money)
    sum = sum + money
#全年销售总额
print("全年销售总额为：",sum)
print("***************************************************************************")

#每种衣服的销售总额
for c in closh:
    data = closhMoney(c)
    print(c,"的销售总额额为：",data[0])
    sa = sa + data[1]
    sale.append(data[1])
print("***************************************************************************")
#每季度销售额占比
for key,value in enumerate(volume):
    if key>=0 and key<3:
        su[0] = su[0] + value
    elif key>=3 and key<6:
        su[1] = su[1] + value
    elif key>=6 and key<9:
        su[2] = su[2] + value
    elif key>=9 and key<12:
        su[3] = su[3] + value
for key,value in enumerate(su):
    print("第",key+1,"季度销售额占比为：",value,"%")

print("***************************************************************************")
#每种衣服的销量占比
for key,value in enumerate(closh):
    print(value,"的销售量占比为",(100*sale[key])/sa,"%")



