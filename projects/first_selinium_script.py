from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
print('sample test case started')


#Following are the sample code for opening the Google Chrome browser:
driver = webdriver.Chrome(ChromeDriverManager().install())

#In the next step, we will be maximizing our browser window size, and the sample code is as below:
driver.maximize_window()

# navigate to the given URL.
driver.get("http://127.0.0.1:8000/$")

# identify button and insert new employee
insert_button = driver.find_element_by_name('insert')
insert_button.click()

#insert Data in different fields
eno = driver.find_element_by_name('eno').send_keys('444')
ename = driver.find_element_by_name('ename').send_keys('Hussain')
esal = driver.find_element_by_name('esal').send_keys('50000')
eaddr = driver.find_element_by_name('eaddr').send_keys('latur')
time.sleep(3)
insert_record = driver.find_element_by_name('record')
insert_record.click()

time.sleep(5)

delete_record = driver.find_element_by_name('del')
delete_record.click()

# driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
time.sleep(15)

#close the browser
driver.close()

print("Sample test case succesfuly completed")
