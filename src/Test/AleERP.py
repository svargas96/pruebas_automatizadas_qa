# important libraries
from selenium import webdriver
import unittest
import time


class TestInicio(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('../drivers/chromedriver.exe')

    def test_login(self):
        driver = self.driver
        driver.get('https://qa.nuevoerp.co/login')
        driver.find_element_by_xpath('/html/body/app-root/app-login/div/div[4]/div/div/form/div[2]/div/input').clear()
        driver.find_element_by_xpath(
            '/html/body/app-root/app-login/div/div[4]/div/div/form/div[2]/div/input').send_keys('crisfalt@gmail.com')
        driver.find_element_by_name('password').clear()
        driver.find_element_by_name('password').send_keys('crisfalt')

        time.sleep(10)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
