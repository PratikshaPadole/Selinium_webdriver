from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
import os
serv_obj=Service("C:\Driver\chromedriver_win32 (2)\chromedriver1.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/")
#driver.save_screenshot('D:\\pythonProject\\DAY1\\lecture_13\\homepage.png')# copy reference path of current directory

driver.save_screenshot(os.getcwd()+"\\homepage.png")
#driver.get_screenshot_as_file(os.getcwd()+"\\homepage.png")


driver.close()                                                             #name of webpage which screenshot we have to click