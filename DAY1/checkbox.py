from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Driver\chromedriver_win32 (2)\chromedriver1.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("https://codepen.io/roshanpatel88/pen/KzaNBM")
driver.maximize_window()
#select specific checkbox

#driver.find_element(By.XPATH,"//input[@value='Automation']").click()
#select all checkbox
#checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
#print(len(checkboxes))
#for checkbox in checkboxes:
#    checkbox.click()
#for i in range(len(checkboxes)):
 #   checkboxes[i].click()


checkboxes = driver.find_elements(By.XPATH,'//input[@type="checkbox"]')
print(len(checkboxes))
#for checkbox in checkboxes:
#    checkbox.click()
driver.close()