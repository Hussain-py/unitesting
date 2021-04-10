from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import unittest
import HtmlTestRunner

class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(2)
        cls.driver.maximize_window()

    def test_search_python(self):
        self.driver.get("https://www.google.com/")
        self.driver.find_element_by_name('q').send_keys("Selenium with Python")
        self.driver.find_element_by_name("btnK").click()
        time.sleep(3)

    def test_search_Automation(self):
        self.driver.get("https://www.google.com/")
        self.driver.find_element_by_name('q').send_keys("AI with Python")
        self.driver.find_element_by_name("btnK").click()
        time.sleep(3)


    @classmethod
    def tearDowClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Hussain/DjangoProjects/selenium/reports'))
