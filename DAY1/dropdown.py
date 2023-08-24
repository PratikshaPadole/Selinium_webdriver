import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service("C:\Driver\chromedriver_win32 (2)\chromedriver1.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
#alloptions=driver.find_elements(By.XPATH,"//select[@id='country']/option")
#print(len(alloptions))
#for opt in alloptions:
#    print(opt.text)
#time.sleep(5)
#for opt in alloptions:
 #   if opt.text=='india':
 #       opt.click()
  #      break


country_ele=driver.find_element(By.XPATH,'//select[@id="country"]')
drpcountry=Select(country_ele)

#select option from dropdown
#drpcountry.select_by_visible_text("Japan")
#drpcountry.select_by_value("france")
drpcountry.select_by_index(1)
time.sleep(5)
driver.close()