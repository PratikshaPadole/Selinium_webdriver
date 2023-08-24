from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Driver\chromedriver_win32 (2)\chromedriver1.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)#time in second
driver.get("https://www.flipkart.com/")
driver.maximize_window()
searchbox = driver.find_element(By.NAME,"q")
searchbox.send_keys("mobiles")
searchbox.submit() # submit use like enter key
driver.find_element(By.XPATH,"//*[text()='SAMSUNG Galaxy F04 (Jade Purple, 64 GB)']").click()
driver.close()