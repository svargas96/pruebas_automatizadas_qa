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
        driver.find_element_by_xpath("//*[@id='frmInicioSesion']/div[2]/div/input").clear()
        driver.find_element_by_xpath(
            "//*[@id='frmInicioSesion']/div[2]/div/input").send_keys('svargasmurcia.sinergia@gmail.com')
        driver.find_element_by_name('password').clear()
        driver.find_element_by_name('password').send_keys('svargas')
        time.sleep(10)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
