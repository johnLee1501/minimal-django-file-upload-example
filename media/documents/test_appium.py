import unittest
from appium import webdriver

from media.documents.BaseRunner import ParametrizedTestCase


class EribankTest(ParametrizedTestCase):
    def testFirstOpen(self):
        if len(self.driver.find_elements_by_xpath("//*[@text='OK']")) > 0:
            self.driver.find_element_by_xpath("//*[@text='OK']").click()
        self.driver.find_element_by_xpath("//*[@text='Username']").send_keys('company')
        self.driver.find_element_by_xpath("//*[@text='Password']").send_keys('company')
        self.driver.find_element_by_xpath("//*[@text='Login']").click()

    @classmethod
    def setUpClass(cls):
        super(EribankTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(EribankTest, cls).tearDownClass()
