from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
from day14.ICBCBank import bank

'''
    DDT:data driver test
        ddt
        data
        unpack
    1.测试类必须用@ddt修饰
    2.测试方法使用@data引入数据源
    任务：
        将工行系统的核心业务进行测试？
        bank_addUser()

'''
# 数据源
add = [
    [12345678,"小明",33334444,"中国","河南","jd","门派",3000]
]
da = [
    [4894894, 100],
    [713544, 300],
    [1123444, 2000]
]
draw = [
    [713544,123456,100],
    [4894894,456789,200]
]

transfer = [
    [713544, 123456,4894894, 100]
]

query = [
    [713544,123456],
    [4894894,456789]
]


@ddt  # 注解，注释这个类是参数化类
class TestCalc(TestCase):
    @data(*add)  # 引入数据源
    @unpack
    def testbank_addUser(self, account, username, password, country, province, street, gate, money):
        # 2.调用被测方法
        Bank = bank()
        Bank.bank_addUser(account, username, password, country, province, street, gate, money)
        # 3.断言

    @data(*da)  # 引入数据源
    @unpack
    def testbank_saveMoney(self, account1, savemoney1):
        # 2.调用被测方法
        Bank = bank()
        Bank.bank_saveMoney(account1, savemoney1)
        # 3.断言

    @data(*draw)  # 引入数据源
    @unpack
    def testbank_drawMoney(self, account, password, draw):
        # 2.调用被测方法
        Bank = bank()
        Bank.bank_drawMoney(account, password, draw)
        # 3.断言

    @data(*transfer)  # 引入数据源
    @unpack
    def testbank_transfer(self,account, password, transfer_account, transfer_money):
        # 2.调用被测方法
        Bank = bank()
        Bank.bank_transfer(account, password, transfer_account, transfer_money)
        # 3.断言

    @data(*query)  # 引入数据源
    @unpack
    def testbank_query(self, account, password):
        # 2.调用被测方法
        Bank = bank()
        Bank.bank_query(account, password)
        # 3.断言