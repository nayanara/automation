import xlrd 
import urllib
from selenium import webdriver
import time
from PIL import Image


# Give the location of the file 
loc = ("/home/mahiti/Desktop/programs/ICFN/CSO_details.xlsx") 
  
host= "https://icfn.in/"
# To open Workbook 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0)

browser = webdriver.Chrome()
browser.maximize_window()


for i in range(sheet.nrows): 

	url = host+str(sheet.cell_value(i, 2))+"/"+str(sheet.cell_value(i, 0))
	print(url)
	browser.get(url)
	time.sleep(10)
	img = browser.find_element_by_xpath("/html/body/app-root/app-cso-details/div/div/section[1]/div/div/div[1]/div/img")
	src = img.get_attribute('src')
	filename=  '/home/mahiti/icfn-dwld/'+str(sheet.cell_value(i, 0))+".png"
	urllib.urlretrieve(src, filename)

driver.close()