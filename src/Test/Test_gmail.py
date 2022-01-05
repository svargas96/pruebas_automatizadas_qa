from selenium import webdriver
import unittest
import time

class TestInicio(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('../drivers/chromedriver.exe')

    def test_login(self):
        driver = self.driver
        driver.get('https://www.google.com/intl/es-419/gmail/about/')
        driver.find_element_by_xpath('/html/body/header/div/div/div/a[2]').click()
        driver.find_element_by_id('identifierId').clear()
        driver.find_element_by_id('identifierId').send_keys("svargasmurcia.sinergia@gmail.com")
        driver.find_element_by_xpath("//*[@id='identifierNext']/div/button").click()
        time.sleep(220)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
