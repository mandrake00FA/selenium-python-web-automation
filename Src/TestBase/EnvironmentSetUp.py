__author__ = 'Enrique Cosio'

import datetime
import unittest
from selenium import webdriver

class EnvironmentSetup(unittest.TestCase):

# Browser attributes
    def setUp(self):
        self.driver = webdriver.Chrome("C:\path_to_driver\chromedriver.exe")
        print ("Run Started at :"+str(datetime.datetime.now()))
        print("Chrome Environment Set Up")
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()

# Close all browser instances and quit
    def tearDown(self):
     if (self.driver!=None):
        print("Test Environment Destroyed")
        print("Run Completed at :" + str(datetime.datetime.now()))
        self.driver.close()
        self.driver.quit()
