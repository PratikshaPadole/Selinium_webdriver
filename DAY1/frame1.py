import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Driver\chromedriver_win32 (2)\chromedriver1.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?index-all.html")
driver.maximize_window()
driver.switch_to.frame("packageListFrame")
driver.find_element(By.LINK_TEXT,'org.openqa.selenium').click()
driver.switch_to.default_content()
driver.switch_to.frame('packageFrame')
driver.find_element(By.LINK_TEXT,'AcceptedW3CCapabilityKeys').click()
driver.switch_to.default_content()
time.sleep(5)
driver.switch_to.frame('classFrame')
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/main/div/dl[2]/dt[25]/span/a").click()
driver.switch_to.default_content()
time.sleep(5)
driver.close()