import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Driver\chromedriver_win32 (2)\chromedriver1.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
time.sleep(5)
#driver.find_element(By.LINK_TEXT,'Books').click()
#driver.find_element(By.PARTIAL_LINK_TEXT,'Digital').click()
#How to find total number of link
links = driver.find_elements(By.TAG_NAME,'a')
print(len(links))
for link in links:
    print(link.text)
time.sleep(5)
driver.close()