from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj=Service("C:\Driver\chromedriver_win32 (2)\chromedriver1.exe")
driver=webdriver.Chrome(service=serv_obj)
mywait=WebDriverWait(driver,10)
driver.get("https:www.flipkart.com")
driver.maximize_window()
searchbox=driver.find_element(By.NAME,'q')
searchbox.send_keys("women dress")
searchbox.submit()
searchlink = mywait.until(EC.presence_of_element_located(By.XPATH,'//*[text()="")'))
searchlink.click()
driver.close()