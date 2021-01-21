import os
import unittest
from appium import webdriver

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def appium_testcase(devices):
    remote = "http://127.0.0.1:4723/wd/hub"
    driver = webdriver.Remote(remote, devices)
    return driver


class ParametrizedTestCase(unittest.TestCase):
    """ TestCase classes that want to be parametrized should  
        inherit from this class.  
    """

    def __init__(self, methodName='runTest', param=None):
        super(ParametrizedTestCase, self).__init__(methodName)
        global devicess
        devicess = param

    @classmethod
    def setUpClass(cls):
        pass
        cls.driver = appium_testcase(devicess)
        cls.devicesName = devicess["deviceName"]

    def setUp(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.close_app()
        cls.driver.quit()
        pass

    def tearDown(self):
        pass

    @staticmethod
    def parametrize(testcase_klass, param=None):
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_klass(name, param=param))
        return suite
