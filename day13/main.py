'''
    报告：
        1.加载器：加载所有测试用例并得到所有用例
        2.使用运行器运行这些测试用例并生成报告
    任务2：
        减乘除：进行测试（）
        实现报告的邮件发送
'''
from HTMLTestRunner import HTMLTestRunner  # 运行器
import unittest

# 1.加载所有用例
tests = unittest.defaultTestLoader.discover(r"E:\python\pythonProject\day13",pattern="test*.py")

# 2.使用运行器
runner = HTMLTestRunner.HTMLTestRunner(
    title = "这是一份计算器的测试报告",
    description="这只是加减乘除的测试报告",
    verbosity=1,
    stream= open("TEST.html",mode="w+",encoding="utf-8")
)

# 3.运行所有用例
runner.run(tests)


# 4.实现邮件发送





