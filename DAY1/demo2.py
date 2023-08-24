import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("C:\Driver\chromedriver_win32 (2)\chromedriver1.exe")

driver = webdriver.Chrome(service = serv_obj)
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")

driver.maximize_window()
#driver.find_element(By.LINK_TEXT,"Become a Seller").click()
#driver.find_element(By.PARTIAL_LINK_TEXT,"").click()
#driver.find_element(By.NAME,"q").send_keys("mens-shirt")
#driver.find_element(By.XPATH,"//button[@class='L0Z3Pu']").click()
#text_element=driver.find_element(By.XPATH,'//*[@id="bse-cd"]/h5/self::h5').text
#print(text_element)
#time.sleep(10)
#driver.find_elements(By.XPATH,"//img[@class='_396cs4']")
#links=driver.find_elements(By.TAG_NAME,'a')
#print(len(links))

#self
#text_1=driver.find_element(By.XPATH,'//*[@id="leftcontainer"]/table/tbody/tr[31]/td[1]/a/self::a').text
#print(text_1)
#parent
#text_msg=driver.find_element(By.XPATH,'//*[@id="leftcontainer"]/table/tbody/tr[31]/td[1]/a/parent::td').text
#print(text_msg)
#ancestor element find data of all child element
childs=driver.find_elements(By.XPATH,'//*[@id="leftcontainer"]/table/tbody/tr[38]/td[1]/a/ancestor::tr/child::td')
print(len(childs))

#ancestor
driver.find_element(By.XPATH,)

driver.close()
