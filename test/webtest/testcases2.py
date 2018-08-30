import unittest
import time
from selenium import webdriver

class TestCase(unittest.TestCase):

    def test_web3(self):
        chromedriver = "webdriver/geckodriver.exe"
        driver = webdriver.Firefox(executable_path=chromedriver)
        driver.maximize_window()
        driver.get("https://www.baidu.com/")
        search_box=driver.find_element_by_id('kw')
        search_box.send_keys('test3')
        search_box.submit()
        time.sleep(3)
        self.assertTrue(driver.current_url.startswith('https://www.baidu.com/'),'redirect error')
        driver.quit()

    def test_web4(self):
        chromedriver = "webdriver/geckodriver.exe"
        driver = webdriver.Firefox(executable_path=chromedriver)
        driver.maximize_window()
        driver.get("https://www.baidu.com/")
        search_box = driver.find_element_by_id('kw')
        search_box.send_keys('test4')
        search_box.submit()
        time.sleep(3)
        self.assertTrue(driver.current_url.startswith('https://www.baidu.com/'), 'redirect error')
        driver.quit()
