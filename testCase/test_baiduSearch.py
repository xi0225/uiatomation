# coding=utf-8
from selenium import webdriver
import time
import unittest


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe')
        self.driver.maximize_window()
        self.driver.get("https://www.baidu.com//")

    def tearDown(self):
        self.driver.close()

    def test_search(self):
        self.driver.find_element_by_id("kw").send_keys("hello")
        self.driver.find_element_by_id("su").click()
        time.sleep(2)
        self.assertIn("hello", self.driver.page_source)

    def test_search1(self):
        self.driver.find_element_by_id("kw").send_keys("hello")
        self.driver.find_element_by_id("su").click()
        time.sleep(2)
        self.assertIn("hello1232323", self.driver.page_source)

    def test_search2(self):
        self.driver.find_element_by_id("k").send_keys("hello")
        self.driver.find_element_by_id("su").click()
        time.sleep(2)
        self.assertIn("hello", self.driver.page_source)


if __name__ == '__main__':
    unittest.main()

