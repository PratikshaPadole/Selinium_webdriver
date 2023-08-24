import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("C:\Driver\chromedriver_win32 (2)\chromedriver1.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()
min_slider=driver.find_element(By.XPATH,'//span[@class="ui-slider-handle ui-corner-all ui-state-default"][1]')
max_slider=driver.find_element(By.XPATH,'//span[@class="ui-slider-handle ui-corner-all ui-state-default"][2]')
print(min_slider.location)#{'x':59,'y':250}
print(max_slider.location)#{'x':412,'y':250}
act=ActionChains(driver)
act.drag_and_drop_by_offset(min_slider,100,0).perform()
act.drag_and_drop_by_offset(max_slider,-150,0).perform()
print(min_slider.location)#{'x':158,'y':250}
print(max_slider.location)#{'x':260,'y':250}
time.sleep(5)
driver.close()