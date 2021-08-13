from unittest import TestCase
from selenium import webdriver
from ddt import ddt
from ddt import data
from ddt import unpack
from 自动化01.day03_2.InitTeacherPage import InitTeacherPage
from 自动化01.day03_2.TeacherLoginPage import TeacherLoginPage
import time

@ddt
class TestTeacherLogin(TestCase):
    #在每个操作前先做准备
    def setUp(self) -> None:
        self.driver=webdriver.Chrome()
        #进入网站
        self.driver.get("http://localhost:8080/HKR")
        time.sleep(2)
        #点击教师登录
        self.driver.find_element_by_link_text("教师登录").click()

    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.quit()

    @data(*InitTeacherPage.login_sucess_data)
    def testTeacherLoginsucess(self,testdata):
            username=testdata["username"]
            password=testdata["password"]
            expect = testdata["expect"]

            #操作类
            Login = TeacherLoginPage(self.driver)
            Login.login(username,password)

            #获取实际结果
            result = Login.get_succes_data()
            self.driver.save_screenshot("sucess.png")
            #断言
            self.assertEqual(expect,result)


    @data(*InitTeacherPage.login_error_data)
    def testTeacherLoginerror(self, testdata):
        username = testdata["username"]
        password = testdata["password"]
        expect = testdata["expect"]

        # 操作类
        Login = TeacherLoginPage(self.driver)
        Login.login(username, password)

        # 获取实际结果
        result = Login.get_error_data()
        self.driver.save_screenshot("error.png")
        # 断言
        self.assertEqual(expect, result)
