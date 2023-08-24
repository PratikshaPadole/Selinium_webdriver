import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Driver\chromedriver_win32 (2)\chromedriver1.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

driver.find_element(By.XPATH,'//input[@name="username"]').send_keys("Admin")
driver.find_element(By.XPATH,'//input[@name="password"]').send_keys("admin123")
time.sleep(5)
driver.find_element(By.XPATH,'//button[@class="oxd-button oxd-button--medium oxd-button--main orangehrm-login-button"]').click()
admin=driver.find_element(By.XPATH,'//a[@class="oxd-main-menu-item active toggle"]/span')
#admin=driver.find_element(By.LINK_TEXT,'Admin')
usermanagement=driver.find_element(By.XPATH,'//li[@class="oxd-topbar-body-nav-tab --parent --visited"]/span"]')
Users=driver.find_element(By.XPATH,"//a[text()='Users']")

#usermanagement=driver.find_element(By.XPATH,"//li/span[text()='User Management']")

#Users=driver.find_element(By.XPATH,'//ul[@class="oxd-dropdown-menu"]/li/a')
act=ActionChains(driver)
act.move_to_element(admin).move_to_element(usermanagement).move_to_element(Users).click().perform()
driver.close()