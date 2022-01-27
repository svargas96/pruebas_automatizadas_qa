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
        driver.find_element_by_xpath("//body/app-root[1]/app-login[1]/div[1]/div[4]/div[1]/div[1]/form[1]/div[2]/div[1]/input[1]").clear()
        driver.find_element_by_xpath("//body/app-root[1]/app-login[1]/div[1]/div[4]/div[1]/div[1]/form[1]/div[2]/div[1]/input[1]").send_keys('prueba@gmail.com')
        driver.find_element_by_xpath("//body/app-root[1]/app-login[1]/div[1]/div[4]/div[1]/div[1]/form[1]/div[3]/div[1]/input[1]").clear()
        driver.find_element_by_xpath("//body/app-root[1]/app-login[1]/div[1]/div[4]/div[1]/div[1]/form[1]/div[3]/div[1]/input[1]").send_keys('prueba12345')
        driver.find_element_by_xpath("//button[contains(text(),'Ingresar')]").click()
        time.sleep(10)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
