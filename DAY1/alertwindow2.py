import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Driver\chromedriver_win32 (2)\chromedriver1.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Confirm']").click()
alertwindow=driver.switch_to.alert
time.sleep(5)
print(alertwindow.text)
alertwindow.accept()
time.sleep(5)
driver.close()