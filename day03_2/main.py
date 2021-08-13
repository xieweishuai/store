from HTMLTestRunner import HTMLTestRunner
import unittest
import os


#获取所有的用例
tests = unittest.defaultTestLoader.discover(os.getcwd(),pattern="Test*.py")


#加载器
runner = HTMLTestRunner.HTMLTestRunner(
         title="这是一个HKR的测试报告",
         description="这是一个详细教师登陆的测试报告",
         verbosity=1,
         stream = open(file="教师登陆测试报告.html",mode="w+",encoding="utf-8")
)

runner.run(tests)
