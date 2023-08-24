#conditional commands
from selenium import webdriver
from selenium .webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Driver\chromedriver_win32 (2)\chromedriver1.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https:demo.nopcommerce.com/register")
driver.maximize_window()
searchbox= driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
print("display status :",searchbox.is_displayed())
print("enable status :",searchbox.is_enabled())
rd_male=driver.find_element(By.XPATH,"//*[@id='gender']/span[1]/label")
rd_female = driver.find_element(By.XPATH,"//*[@id='gender']/span[2]/label")
print("before selected ")
print(rd_male.is_selected())
print(rd_female.is_selected())
print("After selected :")
rd_male.click()
rd_female.click()
print(rd_male.is_selected())
print(rd_female.is_selected())