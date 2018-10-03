__author__ = 'Enrique Cosio'

from selenium.webdriver.common.by import By
from selenium-python-web-automation.Src.PageObject.Locators import Locator


class Home(object):

    def __init__(self, driver):
        self.driver = driver
        # Home page locators definition
        # Locate element by XPath
        self.logo = driver.find_element(By.XPATH, Locator.logo)
        self.orders_link = driver.find_element(By.XPATH, Locator.orders_link)
        self.search_bar = driver.find_element(By.XPATH, Locator.search_bar)
        # Locate element by Class Name
        self.search_button = driver.find_element(By.CLASS_NAME, Locator.search_button)
       
        # Logo
        def getLogo(self):
        return self.logo
        
        # Orders link
        def getOrders(self):
        return self.orders_link

        # Search bar
        def setSearchBar(self, product_name):
        self.search_bar.clear()
        self.search_bar.send_keys(product_name)

        # Submit search button
        def submitProductSearch(self):
        self.search_button.click()
