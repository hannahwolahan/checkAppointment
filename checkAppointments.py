
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

earliest_appointment = "12 May 2022"
# BONDI_JUNCTION = 

driver = webdriver.Chrome('chromedriver')

sitepath = 'https://bmvs.onlineappointmentscheduling.net.au/oasis/'

driver.get(sitepath)
print (driver.find_element_by_id('ContentPlaceHolder1_btnInd'))
# driver.find_element(By.XPATH('ContentPlaceHolder1_btnInd')).click()
driver.find_element_by_id('ContentPlaceHolder1_btnInd').click()
driver.find_element_by_id('ContentPlaceHolder1_SelectLocation1_txtSuburb').send_keys("2024")
state = driver.find_element_by_id('ContentPlaceHolder1_SelectLocation1_ddlState')
state.send_keys("NSW")
state.send_keys(Keys.RETURN)
state.send_keys(Keys.RETURN)
time.sleep(2)
#clinicLocation = driver.find_element_by_id('rbLocation166.rbLocation')
driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_SelectLocation1_divLocations"]/div/table/tbody/tr[1]').click()
driver.switch_to.alert.accept()
driver.find_element_by_id('ContentPlaceHolder1_btnCont').click()
driver.find_element_by_xpath('//*[@id="chkClass1_489"]').click()
driver.find_element_by_xpath('//*[@id="chkClass1_492"]').click()
driver.find_element_by_xpath('//*[@id="chkClass1_498"]').click()
driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_btnCont"]').click()

print("hello")


appDate = (driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_SelectTime1_divSearchResults"]/div[1]/h2')).get_attribute('innerHTML')

appTime = (driver.find_elements_by_xpath('/html/body/form/div[3]/div[2]/div[2]/div[3]/div[2]/table/tbody/tr/td/label'))

print ("len - ",appDate)

for availTimes in appTime:
    print (availTimes.get_attribute('innerHTML'))



# i=0
# while(i<len(appTime)):
#     print(appTime)
#     i=i+1

# soup = BeautifulSoup(html)
# nextAppt = soup.find_all()
# nextTime = soup.find_all('div', {"id": "ContentPlaceHolder1_SelectTime1_divSearchResults"})

# i=0
# print ("LENGTH:   ",len(nextTime))
# while i < len(nextTime):
#     print("Next appointment is ", nextAppt[i])
#     i=i+1

# site="https://bmvs.onlineappointmentscheduling.net.au/oasis/AppointmentTime.aspx"

driver.close()