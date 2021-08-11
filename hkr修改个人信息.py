from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://localhost:8080/HKR")
driver.find_element_by_xpath("//*[@id='loginname' and @name='loginname']").send_keys("root")
driver.find_element_by_xpath("//*[@id='password' and @name='password']").send_keys("root")
driver.find_element_by_xpath("//*[@type='submit' and @id='submit' and @value='登陆']").click()
driver.maximize_window()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='_easyui_tree_8']/span[4]/a").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[1]/td[2]/input").send_keys("root")
driver.find_element_by_xpath("//*[@name='password']").send_keys("root")
driver.find_element_by_xpath("//*[@id='_easyui_textbox_input1']").send_keys("39")
driver.find_element_by_name("sex").send_keys("女")
driver.find_element_by_name("address").send_keys("河南")
driver.find_element_by_name("email").clear()
driver.find_element_by_name("email").send_keys("2021566362@qq.com")
driver.find_element_by_name("carte").send_keys("fvvhgrvfvfdbrh")
driver.find_element_by_id("btn_modify").click()

driver.quit()