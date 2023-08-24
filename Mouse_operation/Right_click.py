import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("C:\Driver\chromedriver_win32 (2)\chromedriver1.exe")
driver=webdriver.Chrome(service=serv_obj)
#driver.implicitly_wait(10)
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
button=driver.find_element(By.XPATH,'//span[@class="context-menu-one btn btn-neutral"]')
act=ActionChains(driver)

act.context_click(button).perform()
driver.find_element(By.XPATH,'//li[@class="context-menu-item context-menu-icon context-menu-icon-copy"]/span').click()
myalert=driver.switch_to.alert
time.sleep(3)
myalert.accept()
time.sleep(3)
driver.close()