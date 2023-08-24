import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("C:\Driver\chromedriver_win32 (2)\chromedriver1.exe")
driver=webdriver.Chrome(service=serv_obj)
#driver.implicitly_wait(10)
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()
rome=driver.find_element(By.XPATH,'//div[@id="box7"]')
italy=driver.find_element(By.XPATH,'//div[@id="box106"]')
act=ActionChains(driver)
act.drag_and_drop(rome,italy).perform()
time.sleep(5)
driver.close()
