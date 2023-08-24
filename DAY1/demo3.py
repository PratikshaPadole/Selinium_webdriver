#Application commands.
from selenium import webdriver
from selenium .webdriver.chrome.service import Service
serv_obj = Service("C:\Driver\chromedriver_win32 (2)\chromedriver1.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("http://opensource-demo.orangehrmlive.com")
print(driver.title)
print(driver.current_url)
print(driver.page_source)
driver.close()
