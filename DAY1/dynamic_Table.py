import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Driver\chromedriver_win32 (2)\chromedriver1.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
#time.sleep(5)
driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
#time.sleep(5)
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[text()=' Login ']").click()
#time.sleep(5)
driver.find_element(By.LINK_TEXT,'Admin').click()
#time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span').click()
time.sleep(2)
driver.find_element(By.XPATH,"//a[text()='Users']").click()
time.sleep(2)

driver.close()


