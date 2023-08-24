from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
import os

from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Driver\chromedriver_win32 (2)\chromedriver1.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/")
reglink =keys.CONTROL + keys.RETURN
driver.find_element(By.LINK_TEXT,'Register').send_keys(reglink)