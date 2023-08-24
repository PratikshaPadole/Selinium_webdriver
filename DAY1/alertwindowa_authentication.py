import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
serv_obj=Service("C:\Driver\chromedriver_win32 (2)\chromedriver1.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(5)
driver.maximize_window()
time.sleep(5)
driver.close()