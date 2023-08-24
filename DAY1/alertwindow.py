import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Driver\chromedriver_win32 (2)\chromedriver1.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
#open alert window
driver.find_element(By.XPATH,'//button[normalize-space()="Click for JS Prompt"]').click()
time.sleep(5)
alertwindow = driver.switch_to.alert
print(alertwindow.text)
alertwindow.send_keys("hello miss ")
#alertwindow.accept()#there print hello miss
alertwindow.dismiss()# there print null
time.sleep(5)
driver.close()