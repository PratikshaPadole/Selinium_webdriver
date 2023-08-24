#navigation commands
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
serv_obj=Service("C:\Driver\chromedriver_win32 (2)\chromedriver1.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://www.snapdeal.com")
driver.get("https://www.amazon.com")
time.sleep(5)

driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)
driver.refresh()
driver.quit()