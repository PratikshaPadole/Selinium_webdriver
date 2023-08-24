import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://www.facebook.com/?stype=lo&jlou=Aff2FBooXVBWMOLJksRrBXo9UcDYoqE36cwLN2WodVEOtH7BHM1gnlKvIed3-Cxe2sq1r64Q2p8lvjWWxIvR9vijv4b2enizAqIN1atgNyRe2A&smuh=28460&lh=Ac8WcUhGa5Pg0dNIln4")
#driver.find_element(By.ID,'APjFqb').send_keys('python')
time.sleep(10)
driver.find_element(By.ID,'email').send_keys('123@pgmail.com')
time.sleep(10)
driver.find_element(By.XPATH,'//input[@name="pass"]').send_keys('999888QA')
time.sleep(5)
driver.find_element(By.XPATH,'//button[@value="1"]').click()
time.sleep(15)

driver.maximize_window()
driver.close()
#driver.implicitly_wait(10)
#driver.find_element(By.XPATH,'//input[@value="Google Search"]').click()
#driver.implicitly_wait(10)