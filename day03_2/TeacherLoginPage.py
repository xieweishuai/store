class TeacherLoginPage:
    def __init__(self,driver):
        self.driver=driver   #将driver改为全局变量

    def login(self,username,password):
        #输入用户名
        self.driver.find_element_by_id("loginname").send_keys(username)
        #输入密码
        self.driver.find_element_by_id("password").send_keys(password)
        #点击登录
        self.driver.find_element_by_id("submit").click()

    def get_succes_data(self):
        #返回窗口标题
        return self.driver.title

    def get_error_data(self):
        #返回失败提示
        return self.driver.find_element_by_id("msg_uname").text
