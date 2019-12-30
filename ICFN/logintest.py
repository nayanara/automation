from selenium import webdriver
import time

#driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.get('https://icfn3uiv1.mahiti.org/login')
driver.maximize_window()
credentials = [('ss','aa'),('aa','aa')]



driver.find_element_by_xpath('/html/body/app-root/app-login-page/div/div/div/div/div/form/div[1]/div/div/input').send_keys('sss')
driver.find_element_by_xpath('/html/body/app-root/app-login-page/div/div/div/div/div/form/div[2]/div/input').send_keys('ss')
driver.find_element_by_xpath('/html/body/app-root/app-login-page/div/div/div/div/div/form/div[3]/div/div/div[2]/div/button').click()
time.sleep(10)
driver.find_element_by_xpath('/html/body/app-root/app-partner-dashboard/app-headerbar/div/div[2]/p/a').click()
time.sleep(10)
driver.find_element_by_xpath('//*[@id="user_logout"]/ul/li[2]/a/img').click()




