import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


serv_obj=Service("C:\Driver\chromedriver_win32 (2)\chromedriver1.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
driver.find_element(By.xpath,'//span[@id="select2-billing_country-container"]').click()
time.sleep(5)
driver.find_element(By.XPATH,'(//li[@class="select2-results__option"])[87]').click()
time.sleep(5)
driver.close()
