import unittest

from pubilc.driver import pcdriver


class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = pcdriver()
        cls.driver.maximize_window()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()