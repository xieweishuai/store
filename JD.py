from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome()
#登录京东
driver.get("https://www.jd.com")
driver.maximize_window()
driver.find_element_by_class_name("link-login").click()
driver.maximize_window()

#账户登录
driver.find_element_by_link_text("账户登录").click()
time.sleep(2)
driver.find_element_by_id("loginname").send_keys("15524531829")
time.sleep(2)
driver.find_element_by_id("nloginpwd").send_keys("998765xws")
time.sleep(2)
driver.find_element_by_id("loginsubmit").click()

time.sleep(6)
driver.maximize_window()
#搜索华为手机
time.sleep(5)
driver.find_element_by_xpath("//*[@id='key']").send_keys("小米二手手机")
driver.find_element_by_xpath("//*[@id='search']/div/div[2]/button").click()

#选择一个商品
time.sleep(3)
driver.find_element_by_class_name("p-img").click()

#窗口切换
#获取所有窗口的句柄
data = driver.window_handles
driver.switch_to.window(data[1])  #切换窗口

#加入购物车
time.sleep(3)
driver.find_element_by_link_text("加入购物车").click()

#去购物车结算
time.sleep(4)
driver.find_element_by_link_text("去购物车结算").click()

#去结算
time.sleep(3)
driver.find_element_by_class_name("common-submit-btn").click()

driver.quit()

