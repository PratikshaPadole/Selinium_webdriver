import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("C:\Driver\chromedriver_win32 (2)\chromedriver1.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
driver.maximize_window()
driver.switch_to.frame("iframeResult")#name=iframeResult
field=driver.find_element(By.XPATH,'//input[@id="field1"]')
field.clear()
field.send_keys("welcome")
button=driver.find_element(By.XPATH,"//button[text()='Copy Text']")
act=ActionChains(driver)
act.double_click(button).perform()
time.sleep(5)
driver.quit()
