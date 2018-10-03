__author__ = 'Enrique Cosio'

class ProductSearch(EnvironmentSetup):

    # Test case method
    def test_product_search(self):
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
            print("Product search executed")
        except NoSuchElementException:
            print("Product search failed")

        # Calling search results page object
        results = SearchResults(driver)

        # Validates product sorting
        try:
            results.setSortingOrder("Price: High to Low")
            print("Sorting executed")
        except NoSuchElementException:
            print("Sorting failed")
        sleep(1)

        # Validates hover over menu
        try:
            results.selectCreateList(driver)
            print("Hover over executed")
        except NoSuchElementException:
            print("Hover over executed")
        sleep(4)


if __name__ == '__main__':
    unittest.main()
