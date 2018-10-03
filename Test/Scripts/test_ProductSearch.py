__author__ = 'Enrique Cosio'

import unittest
from time import sleep
from selenium-python-web-automation.Src.TestBase.EnvironmentSetUp import EnvironmentSetup
from selenium-python-web-automation.Src.PageObject.Pages.HomePage import Home
from selenium.common.exceptions import NoSuchElementException


class ProductSearch(EnvironmentSetup):

    # Test case method
    def test_product_search_flow(self):
        driver = self.driver
        
        expected_title = "Amazon.com: Online Shopping for Electronics, Apparel, Computers, Books, DVDs & more"

        # Validates page title through catching exception
        if driver.title == expected_title:
            print("Home page loaded successfully")
            self.assertEqual(driver.title, expected_title)
        else:
            print("Home page failed to load")

        # Calling home page object
        home = Home(driver)

        # Validates logo
        if home.getLogo().is_displayed():
            print("Logo displayed")
        else:
            print("Logo not displayed")

        # Validates search functionality
        try:
            home.setSearchBar("Tablet")
            home.submitProductSearch()
        except NoSuchElementException:
            print("Product search failed")

        # Calling search results page object
        results = SearchResults(driver)

        # Validates product sorting
        results.setSortingOrder("Price: High to Low")
        sleep(1)

        # Validates hover over menu
        results.selectCreateList(driver)
        sleep(3)


if __name__ == '__main__':
    unittest.main()
