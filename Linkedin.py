#Primer codigo para automatizar el inicio de sesión de Linkedin
from selenium import webdriver
import unittest
import allure
import time

class TestInicio(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('src/drivers/chromedriver.exe')

    def test_login(self):
       driver = self.driver
       driver.get('https://www.linkedin.com/login/es?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
       driver.find_element_by_id('username').clear()
       driver.find_element_by_id('username').send_keys('sergioandres-196@hotmail.com')
       driver.find_element_by_id('password').clear()
       driver.find_element_by_id('password').send_keys('1075297647Sergio')

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()