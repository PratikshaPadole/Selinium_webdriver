#this for browser commands close and quit
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Driver\chromedriver_win32 (2)\chromedriver1.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
time.sleep(10)
driver.close()
#driver.quit()
