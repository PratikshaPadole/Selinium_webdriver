import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Driver\chromedriver_win32 (2)\chromedriver1.exe")
driver=webdriver.Chrome(service=serv_obj)
#driver.implicitly_wait(10)
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
driver.switch_to.frame(0)
driver.find_element(By.XPATH,"//*[@id='datepicker']").click()
year="2020"
month="January"
Date="15"
while True:
    MON =driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    YR =driver.find_element(By.XPATH,'//span[@class="ui-datepicker-year"]').text
    if month == MON and year == YR:
        break
    else:
        driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-w']").click()
dates=driver.find_elements(By.XPATH,'//table[@class="ui-datepicker-calendar"]/tbody/tr/td/a')
for date in dates:
    if date.text==Date:
        date.click()


time.sleep(5)
driver.close()