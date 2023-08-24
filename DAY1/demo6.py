import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Driver\chromedriver_win32 (2)\chromedriver1.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://demo.nopcommerce.com/")
#locator matching with single webelement
element = driver.find_element(By.XPATH,"//*[@id='small-searchterms']")
time.sleep(5)
element.send_keys("HTC One M8 Android L 5.0 Lollipop")
time.sleep(5)
# locator matching with multiple web elements
element = driver.find_element(By.XPATH,"//div[@class='footer']//a")
time.sleep(5)
print(element.text) #sitemap
time.sleep(5)
#element not available then throw NosuchElementException
login_element=driver.find_element(By.LINK_TEXT,"Log ")
time.sleep(5)
login_element.click()
time.sleep(5)
driver.close()