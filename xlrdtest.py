import xlrd
import xlwt
from DBUtils import *
fname = "12月份衣服销售数据.xlsx"
kname = "12月份各种服饰销售情况"
def Excel_to_db(fname,kname):
    # 1. 打开工作簿
    wd = xlrd.open_workbook(filename=fname,encoding_override=True)

    # 2.打开您要操作的选项卡
    st = wd.sheet_by_name(kname)
    # 3.读取数据
    rows = st.nrows  # 获取行数  # 4
    cols = st.ncols  # 获取列数
    for i in range(1,rows):   # 0~4   0 1 2 3
        data=st.row_values(i)
        sql = "insert into sale values(%s,%s,%s,%s,%s) "
        update(sql,data)
    # 4.关闭资源
Excel_to_db(fname,kname)
def Db_to_excel(fname,kname):
    sale = ["日期","服装名称","价格/件","库存数量","销售量/每日"]
    sql = "select * from sale"
    param = []
    data = select(sql, param, mode="all", )
    workbook = xlwt.Workbook(encoding='utf-8')  # Workbook的W是大写的，encoding是编码格式
    # 添加一个sheet1
    rows = len(data)
    cols = len(data[0])
    sheet1 = workbook.add_sheet('12月各种衣服销售情况', cell_overwrite_ok=True)
    i=0
    j=0
    for i in range(rows):
        for j in range(cols):
            if i == 0:
                # 向sheet中写入数据
                 sheet1.write(0, j, sale[j])  # 在第一行的第一列写入hello world
            else:
                # 向sheet中写入数据
                sheet1.write(i, j, data[i-1][j])  # 在第一行的第一列写入hello world
        #
    workbook.save('E:/python/pythonProject/day09/xlwt.xls')
    print('创建excel完成！')
    # 4.关闭资源
Db_to_excel(fname, kname)