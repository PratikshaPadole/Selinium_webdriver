import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


serv_obj=Service("C:\Driver\chromedriver_win32 (2)\chromedriver1.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

#radio button
driver.find_element(By.XPATH,"//input[@id='product_7441']").click()

#value pass
driver.find_element(By.XPATH,"//input[@id='travname']").send_keys("Pratiksha")
driver.find_element(By.XPATH,"//input[@id='travlastname']").send_keys("Padole")
time.sleep(2)
#date
driver.find_element(By.XPATH,"//input[@id='dob']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[@class='ui-datepicker-title']/select[1]/option").click()
time.sleep(2)
mon=Select(driver.find_element(By.XPATH,"//div[@class='ui-datepicker-title']/select[1]"))
time.sleep(2)
mon.select_by_visible_text("Oct")#oct
time.sleep(2)
year=Select(driver.find_element(By.XPATH,"//select[@data-handler='selectYear']"))
time.sleep(2)
year.select_by_visible_text("1996")
time.sleep(2)
dates=driver.find_elements(By.XPATH,'//table[@class="ui-datepicker-calendar"]/tbody/tr/td/a')
for date in dates:
    if date.text == "9":
        date.click()
time.sleep(2)

driver.find_element(By.XPATH,'//input[@id="sex_2"]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//input[@id="traveltype_1"]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//input[@id="fromcity"]').send_keys("Pune")
time.sleep(2)
driver.find_element(By.XPATH,'//input[@id="tocity"]').send_keys("Yavatmal")
time.sleep(2)
driver.find_element(By.XPATH,'//input[@class="thwcfe-checkout-date-picker input-text thwcfe-input-field hasDatepicker"]').click()
time.sleep(2)

# date_month=Select(driver.find_element(By.XPATH,'//select[@data-handler="selectMonth"]'))
# date_month.select_by_index(7)
# time.sleep(2)
# date_year=Select(driver.find_element(By.XPATH,'//select[@data-handler="selectYear"]'))
# date_year.select_by_visible_text("2023")
# time.sleep(2)
# # d=driver.find_elements(By.XPATH,'//table[@class="ui-datepicker-calendar"]/tbody/tr/td/a')
# # for d1 in d:
# #     if d1.text == "3":
# #         d1.click()
#
# dates=driver.find_elements(By.XPATH,'//table[@class="ui-datepicker-calendar"]/tbody/tr/td/a')
# for date in dates:
#     if date.text == "8":
#         date.click()
mon=Select(driver.find_element(By.XPATH,"//div[@class='ui-datepicker-title']/select[1]"))
time.sleep(2)
mon.select_by_visible_text("Oct")#oct
time.sleep(2)
year=Select(driver.find_element(By.XPATH,"//select[@data-handler='selectYear']"))
time.sleep(2)
year.select_by_visible_text("2023")
time.sleep(2)
dates=driver.find_elements(By.XPATH,'//table[@class="ui-datepicker-calendar"]/tbody/tr/td/a')
for date in dates:
    if date.text == "15":
        date.click()

time.sleep(10)
driver.close()






