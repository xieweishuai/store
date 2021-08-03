"""
    单元测试：
        1.unittest单元组件
        1.1 继承TestCase测试用例
        1.2 测试用例方法命名必须是testXXXX
        1.3 使用assertEqual()来断言

"""
import unittest

from day13.Calc import Calc


class TestCalc(unittest.TestCase):

    def testAdd(self):
        # 1.准备数据
        a = 6
        b = 5
        c = -11
        # 2.调用被测程序
        calc = Calc()
        sum = calc.add(a,b)

        # 3.断言
        self.assertEqual(c,sum)

    def testAdd1(self):
        # 1.准备数据
        a = -6
        b = -5
        c = -11
        # 2.调用被测程序
        calc = Calc()
        sum = calc.add(a, b)

        # 3.断言
        self.assertEqual(c, sum)

    def testsubs(self):
        # 1.准备数据
        a = 2
        b = 1
        c = 1
        # 2.调用被测程序
        calc = Calc()
        sum = calc.subs(a, b)

        # 3.断言
        self.assertEqual(c, sum)

    def testsubs1(self):
        # 1.准备数据
        a = -2
        b = -1
        c = -1
        # 2.调用被测程序
        calc = Calc()
        sum = calc.subs(a, b)

        # 3.断言
        self.assertEqual(c, sum)

    def testsubs2(self):
        # 1.准备数据
        a = 1
        b = -2
        c = 3
        # 2.调用被测程序
        calc = Calc()
        sum = calc.subs(a, b)

        # 3.断言
        self.assertEqual(c, sum)

    def testsubs3(self):
        # 1.准备数据
        a = -1
        b = -2
        c = 1
        # 2.调用被测程序
        calc = Calc()
        sum = calc.subs(a, b)

        # 3.断言
        self.assertEqual(c, sum)

    def testmulti(self):
        # 1.准备数据
        a = 1
        b = 2
        c = 2
        # 2.调用被测程序
        calc = Calc()
        sum = calc.multi(a, b)

        # 3.断言
        self.assertEqual(c, sum)

    def testmulti1(self):
        # 1.准备数据
        a = -2
        b = -1
        c = 2
        # 2.调用被测程序
        calc = Calc()
        sum = calc.multi(a, b)

        # 3.断言
        self.assertEqual(c, sum)

    def testmulti2(self):
        # 1.准备数据
        a = 1
        b = -2
        c = -2
        # 2.调用被测程序
        calc = Calc()
        sum = calc.multi(a, b)

        # 3.断言
        self.assertEqual(c, sum)

    def testmulti3(self):
        # 1.准备数据
        a = -1
        b = -2
        c = 1
        # 2.调用被测程序
        calc = Calc()
        sum = calc.multi(a, b)

        # 3.断言
        self.assertEqual(c, sum)

    def testdevision(self):
        # 1.准备数据
        a = 1
        b = 2
        c = 0
        # 2.调用被测程序
        calc = Calc()
        sum = calc.devision(a, b)

        # 3.断言
        self.assertEqual(c, sum)

    def testdevision1(self):
        # 1.准备数据
        a = -2
        b = -1
        c = 2
        # 2.调用被测程序
        calc = Calc()
        sum = calc.devision(a, b)

        # 3.断言
        self.assertEqual(c, sum)

    def testdevision2(self):
        # 1.准备数据
        a = 1
        b = -2
        c = -1
        # 2.调用被测程序
        calc = Calc()
        sum = calc.devision(a, b)

        # 3.断言
        self.assertEqual(c, sum)

    def testdevision3(self):
        # 1.准备数据
        a = -1
        b = -2
        c = 0
        # 2.调用被测程序
        calc = Calc()
        sum = calc.devision(a, b)

        # 3.断言
        self.assertEqual(c, sum)