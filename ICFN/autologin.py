from selenium import webdriver
import time
from credentials import *



def autologin(username,password,driver):
	#driver = webdriver.Firefox()
	# driver = webdriver.Chrome()
	# driver.get('https://icfn3uiv1.mahiti.org/login')
	#driver.maximize_window()
	driver.find_element_by_xpath('/html/body/app-root/app-login-page/div/div/div/div/div/form/div[1]/div/div/input').send_keys(username)
	driver.find_element_by_xpath('/html/body/app-root/app-login-page/div/div/div/div/div/form/div[2]/div/input').send_keys(password)
	driver.find_element_by_xpath('/html/body/app-root/app-login-page/div/div/div/div/div/form/div[3]/div/div/div[2]/div/button').click()
	time.sleep(15)
	
	if driver.current_url == 'https://icfn3uiv1.mahiti.org/login':
		forgotpassword(username,driver)
		print("login unsuccessful resetting password for \t"+ username)		
 	elif driver.current_url == 'https://icfn3uiv1.mahiti.org/partner-dashboard':	
		print("login successfull for the user \t"+ username)
 		driver.find_element_by_xpath('/html/body/app-root/app-partner-dashboard/app-headerbar/div/div[2]/p/a').click()
		time.sleep(15)
		driver.find_element_by_xpath('/html/body/app-root/app-partner-dashboard/app-headerbar/div/div[2]/p/a')
		time.sleep(10)
		driver.find_element_by_xpath('//*[@id="user_logout"]/ul/li[2]/a').click()
		time.sleep(15)
		driver.find_element_by_xpath('/html/body/app-root/app-home-page/app-headerbar/div/div[2]/p[2]/a').click()
	# print("auto login fixed")



def forgotpassword(username,driver):
	print(username+ ' forget password')
	# driver = webdriver.Chrome()
	driver.get('https://icfn3uiv1.mahiti.org/forgot-password/')
	driver.find_element_by_xpath('/html/body/app-root/app-forgot-password/div/div/div/div/div/form/div[1]/div/input').send_keys(username)
	driver.find_element_by_xpath('/html/body/app-root/app-forgot-password/div/div/div/div/div/form/div[2]/div/div/div/div/button').click()
	time.sleep(5)




driver = webdriver.Chrome()
driver.get('https://icfn3uiv1.mahiti.org/login')
for i,j in u_credentials:
	autologin(i,j,driver)
	time.sleep(10)
