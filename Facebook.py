from selenium import webdriver
import unittest
import selectors
import allure
import time

class TestInicio(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')

    def test_login(self):
        driver = self.driver
        driver.get('https://web.facebook.com/')
        driver.find_element_by_id('email').clear()
        driver.find_element_by_id('email').send_keys('sergioandres-196@hotmail.com')
        driver.find_element_by_id('pass').clear()
        driver.find_element_by_id('pass').send_keys('1075297647sergio')

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
