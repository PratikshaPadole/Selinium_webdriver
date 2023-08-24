import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("C:\Driver\chromedriver_win32 (2)\chromedriver1.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://www.countries-ofthe-world.com/flags-of-asia.html")
driver.maximize_window()
#1)Scroll down page by pixel
#driver.execute_script("window.scrollBy(0,700)","")
#value=driver.execute_script("return window.pageYOffset;")
#print(value)#1200
#time.sleep(5)

#2)scroll downpage till the eleent visible
# flag=driver.find_element(By.XPATH,'//img[@alt="Flag of India"]')
# driver.execute_script("arguments[0].scrollIntoView();",flag)
# value=driver.execute_script("return window.pageYOffset;") #it gives the current position of scroll
# print(value)
# time.sleep(5)

#3)scroll down till page end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;") #it gives the current position of scroll
print(value)
time.sleep(5)
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
time.sleep(2)