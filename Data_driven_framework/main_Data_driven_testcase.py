import time

from selenium import webdriver
from selenium .webdriver.chrome .service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Data_driven_framework import XLutils
serv_obj=Service("C:\\Driver\\chromedriver_win32 (2)\\chromedriver.exe")
driver = webdriver.Chrome(service = serv_obj)
driver.implicitly_wait(10)
driver.get("https://www.moneycontrol.com/personal-finance/tools/income-tax-calculator")
driver.maximize_window()
#read data from excel
file="C:\\selenium_Practice\\book3.xlsx"
rows=XLutils.getRowCount(file,"Sheet1")
for r in range(2,rows+1):
    Age=XLutils.readData(file,"Sheet1",r,1)
    residental_status = XLutils.readData(file,"Sheet1",r,2)
    annual_sal=XLutils.readData(file,"Sheet1",r,3)
    buss_income=XLutils.readData(file,"Sheet1",r,4)
    saving_ac_interest=XLutils.readData(file,"Sheet1",r,5)
    other_interest=XLutils.readData(file,"Sheet1",r,6)
    other_income=XLutils.readData(file,"Sheet1",r,7)
    payable_tax=XLutils.readData(file,"Sheet1",r,8)

    #passing data to the application
    driver.find_element(By.XPATH,'//*[@id="age"]')
    #driver.find_element(By.XPATH, '//select[@class="custselect"]').click()
    residental_status_drp=Select(driver.find_element(By.XPATH,'//select[@class="custselect"]'))
    residental_status_drp.select_by_visible_text(residental_status)
    time.sleep(5)
    button=driver.find_element(By.XPATH,'//a[@class="btn_common nextfrm MR10 calculateTax"]')
    driver.execute_script("arguments[0].click();",button)
    driver.find_element(By.XPATH, '//input[@name="annual_salary"]').send_keys(annual_sal)
    driver.find_element(By.XPATH, '//input[@name="business_income"]').send_keys(buss_income)
    driver.find_element(By.XPATH, '//input[@name="saving_bank_interest"]').send_keys(saving_ac_interest)
    driver.find_element(By.XPATH, '//input[@name="other_interest"]').send_keys(other_interest)
    driver.find_element(By.XPATH, '//input[@name="other_income"]').send_keys(other_income)
    button = driver.find_element(By.XPATH, '(//a[@class="btn_common nextfrm calculateTax"])')
    driver.execute_script("arguments[0].click();", button)

    act_tax=driver.find_element(By.XPATH,'//strong/span[@id="display_tax"]').text
    basic_tab=driver.find_element(By.XPATH,'//*[@id="basic_info_tab"]/a')
    driver.execute_script("arguments[0].click();",basic_tab)
    #validation
    # Remove commas and non-breaking space characters
    def convert_string_to_float(value):
        cleaned_value = value.replace(',', '').replace('\xa0', '')
        try:
            return float(cleaned_value)
        except ValueError:
            return  None
    payable_tax_1= convert_string_to_float(payable_tax)
    actual_tax=convert_string_to_float(act_tax)


    # Convert the cleaned value to a float


    if payable_tax_1 == actual_tax:
        print("text passed")
        XLutils.writeData(file,"Sheet1",r,10,"PASSED")
        XLutils.FillGreenColor(file,"Sheet1",r,10)

    else:
        print("text Failed")
        XLutils.writeData(file,"Sheet1",r,10,"Failed")
        XLutils.FillRedClolor(file,"Sheet1",r,10)

    time.sleep(5)
driver.close()

