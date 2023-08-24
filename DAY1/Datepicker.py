import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Driver\chromedriver_win32 (2)\chromedriver1.exe")
driver=webdriver.Chrome(service=serv_obj)
#driver.implicitly_wait(15)
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
driver.switch_to.frame(0)
driver.find_element(By.XPATH,"//*[@id='datepicker']").send_keys("06/12/2022")
time.sleep(5)
driver.close()