from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import unittest
import HtmlTestRunner

class CrudProject_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #Following are the sample code for opening the Google Chrome browser:
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(2)
        cls.driver.maximize_window()

    def test_insert_record(self):
        self.driver.get("http://127.0.0.1:8000/$")
        insert_button = self.driver.find_element_by_name('insert')
        insert_button.click()
        self.driver.find_element_by_name('eno').send_keys('444')
        self.driver.find_element_by_name('ename').send_keys('jhony deep')
        self.driver.find_element_by_name('esal').send_keys('50000')
        self.driver.find_element_by_name('eaddr').send_keys('US')
        insert_record =self.driver.find_element_by_name('record')
        insert_record.click()
        time.sleep(3)
        # self.driver.find_element_by_name('up').click()
        # self.time.sleep(3)

    def test_delete_record(self):
        self.driver.get("http://127.0.0.1:8000/$")
        self.driver.find_element_by_name('del').click()
        time.sleep(3)

    @classmethod
    def tearDowClass(cls):
        cls.driver.close()
        # cls.driver.quit()
        print("Test Completed")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Hussain/DjangoProjects/selenium/reports'))
