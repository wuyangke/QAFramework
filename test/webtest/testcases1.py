import unittest
import time
from selenium import webdriver

class TestCase(unittest.TestCase):

    def test_web1(self):
        chromedriver = "webdriver/chromedriver.exe"
        driver = webdriver.Chrome(executable_path=chromedriver)
        driver.maximize_window()
        driver.get("https://www.baidu.com/")
        search_box=driver.find_element_by_id('kw')
        search_box.send_keys('test1')
        search_box.submit()
        time.sleep(3)
        self.assertTrue(driver.current_url.startswith('https://www.baidu.com/'),'redirect error')
        driver.quit()

    def test_web2(self):
        chromedriver = "webdriver/chromedriver.exe"
        driver = webdriver.Chrome(executable_path=chromedriver)
        driver.maximize_window()
        driver.get("https://www.baidu.com/")
        search_box = driver.find_element_by_id('kw')
        search_box.send_keys('test2')
        search_box.submit()
        time.sleep(3)
        self.assertTrue(driver.current_url.startswith('https://www.baidu.com/'), 'redirect error')
        driver.quit()
