from selenium import webdriver
import time

#driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.get('https://icfn3uiv1.mahiti.org/individual_register')
time.sleep(4)
driver.find_element_by_xpath('/html/body/app-root/app-sign-up/div/section[3]/div/div/section/div/div/form/div[1]/div/select/option[2]').click()
driver.find_element_by_xpath('//html/body/app-root/app-sign-up/div/section[3]/div/div/section/div/div/form/div[2]/div/input').send_keys('Harish')
driver.find_element_by_xpath('/html/body/app-root/app-sign-up/div/section[3]/div/div/section/div/div/form/div[4]/div/input').send_keys('9875632588')
driver.find_element_by_xpath('/html/body/app-root/app-sign-up/div/section[3]/div/div/section/div/div/form/div[5]/div/input').send_keys('nayanasky111@gmail.com')
driver.find_element_by_xpath('/html/body/app-root/app-sign-up/div/section[3]/div/div/section/div/div/form/div[6]/div/input').send_keys('nayana123')
driver.find_element_by_xpath('/html/body/app-root/app-sign-up/div/section[3]/div/div/section/div/div/form/div[7]/div/input').send_keys('nayana123')
driver.find_element_by_xpath('/html/body/app-root/app-sign-up/div/section[3]/div/div/section/div/div/form/div[8]/div/input').send_keys('jayangar 9th block ragigudda')
driver.find_element_by_xpath('/html/body/app-root/app-sign-up/div/section[3]/div/div/section/div/div/form/div[10]/div/select/option[15]').click()
driver.find_element_by_xpath('/html/body/app-root/app-sign-up/div/section[3]/div/div/section/div/div/form/div[12]/div/input').send_keys('Banglore')
driver.find_element_by_xpath('/html/body/app-root/app-sign-up/div/section[3]/div/div/section/div/div/form/div[13]/div/input').send_keys('985632')
driver.find_element_by_xpath('/html/body/app-root/app-sign-up/div/section[3]/div/div/section/div/div/form/div[15]/div/div/button').click()












