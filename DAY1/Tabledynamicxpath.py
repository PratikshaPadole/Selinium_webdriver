from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Driver\chromedriver_win32 (2)\chromedriver1.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
#count number of rows & columns
Noofrows=len(driver.find_elements(By.XPATH,'//*[@id="HTML1"]/div[1]/table/tbody/tr'))
print(Noofrows)
NoOfCoulumns=len(driver.find_elements(By.XPATH,'//*[@id="HTML1"]/div[1]/table/tbody/tr/th'))
print(NoOfCoulumns)
#read specific row & column data
#data=driver.find_element(By.XPATH,'//*[@id="HTML1"]/div[1]/table/tbody/tr[4]/td[1]').text
#data1=driver.find_element(By.XPATH,'//*[@id="HTML1"]/div[1]/table/tbody/tr[4]/td[3]').text
#data2=driver.find_element(By.XPATH,'//*[@id="HTML1"]/div[1]/table/tbody/tr[4]/td[4]').text
#print(data)
#print(data1)
#print(data2)

#3)read all the rows and coloumn data
#datas=driver.find_elements(By.XPATH,'//*[@id="HTML1"]/div[1]/table/tbody/tr/td')
#for data in datas:
 #   print(data.text ,end='   ')
#print()

#with dyanamic xpath
for r in range(2, Noofrows +1):
    for c in range(1,NoOfCoulumns +1):
        data=driver.find_element(By.XPATH,'//table[@name="BookTable"]/tbody/tr["+str(r)+"]/td["+str(c)+"]').text
        print(data,end='   ')
    print()
print(Noofrows)
print(NoOfCoulumns)

#Read data based on condition (List books name whose author is Mukesh )
for r in range(2,Noofrows+1):
    authorname = driver.find_element(By.XPATH,'//table[@name="BookTable"]/tbody/tr["+str(r)+"]/td[2]').text
    if authorname == 'Mukesh':

        bookname = driver.find_element(By.XPATH,'//table[@name="BookTable"]/tbody/tr["+str(r)+"]/td[3]').text
        price = driver.find_element(By.XPATH,'//table[@name="BookTable"]/tbody/tr["+str(r)+"]/td[4]').text
    print(bookname,"    ",authorname,"   ",price)

driver.close()
