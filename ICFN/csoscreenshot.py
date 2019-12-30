import xlrd 
from selenium import webdriver
import time
from PIL import Image
from cStringIO import StringIO

verbose = 1
# Give the location of the file 
loc = ("/home/mahiti/Desktop/programs/ICFN/CSO_details.xlsx") 
  
host= "https://icfn.in/"
# To open Workbook 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
  
# For row 0 and column 0 
print(sheet.cell_value(0, 0))
print(sheet.nrows) 
print(sheet.ncols)

browser = webdriver.Chrome()
browser.maximize_window()
js = 'return Math.max( document.body.scrollHeight, document.body.offsetHeight,  document.documentElement.clientHeight,  document.documentElement.scrollHeight,  document.documentElement.offsetHeight);'


for i in range(sheet.nrows): 
    # print(sheet.cell_value(i, 0),sheet.cell_value(i, 1),sheet.cell_value(i, 2),sheet.cell_value(i, 3))
    # print('-----------')    # print()

	url = host+str(sheet.cell_value(i, 2))+"/"+str(sheet.cell_value(i, 0))
	print(url)
	browser.get(url)
	time.sleep(10)


	#screenshot code
	scrollheight = browser.execute_script(js)

	if verbose > 0: 
	    print scrollheight

	slices = []
	offset = 0
	while offset < scrollheight:

	    if verbose > 0: 
	        print offset

	    browser.execute_script("window.scrollTo(0, %s);" % offset)
	    img = Image.open(StringIO(browser.get_screenshot_as_png()))
	    offset += img.size[1]
	    slices.append(img)

	    if verbose > 0:
	        browser.get_screenshot_as_file('%s/screen_%s.png' % ('/tmp', offset))
	        print scrollheight


	screenshot = Image.new('RGB', (slices[0].size[0], offset))
	offset = 0
	for img in slices:
	    screenshot.paste(img, (0, offset))
	    offset += img.size[1]
	    s = time.time()
	    s_time = str(s).replace('.','')
	    filename=  '/home/mahiti/Desktop/Screenshot/'+str(sheet.cell_value(i, 0))+".png"
	    screenshot.save(filename)

