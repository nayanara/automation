from selenium import webdriver
import time 

driver = webdriver.Chrome()
driver.get('https://icfn.in/csos/TSK25K')
driver.maximize_window()
time.sleep(5)
driver.find_element_by_xpath('/html/body/app-root/app-cso-listing/div/section/div[1]/div[3]/div[2]/div/div/div/div/div[2]/form/div[2]/p/a').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="myModal7"]/div/div/div/div/div/div/div/div/label[1]/span').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="home"]/section[1]/div[1]/form/div/label[4]/span').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="home"]/section[2]/div/div/form/div[1]/div/input').send_keys("Nayana")
driver.find_element_by_xpath('//*[@id="home"]/section[2]/div/div/form/div[2]/div/input').send_keys("nayana.r.a@mahiti.org")
driver.find_element_by_xpath('//*[@id="home"]/section[2]/div/div/form/div[3]/div/input').send_keys('9786577765')
driver.find_element_by_xpath('//*[@id="home"]/section[2]/div/div/form/div[4]/div/input').send_keys('jayanagar')
driver.find_element_by_xpath('//*[@id="home"]/section[2]/div/div/form/div[7]/div/input').send_keys('near ragigudda temple')
driver.find_element_by_xpath('//*[@id="home"]/section[2]/div/div/form/div[8]/div/input').send_keys('985632')
driver.find_element_by_xpath('//*[@id="home"]/section[2]/div/div/form/div[6]/div/select/option[17]').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="home"]/section[2]/div/div/form/div[10]/div/div/button').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="menu1"]/section[2]/div/div/div[2]/div/div/div/input').click()
driver.find_element_by_xpath('//*[@id="rzp-button1"]').click()



#/html/body/app-root/app-cso-listing/div/section/div[1]/div[3]/div[2]/div/div/div/div/div[2]/#form/div[2]/p/a






