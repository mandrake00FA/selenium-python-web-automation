__author__ = 'Enrique Cosio'

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium-python-web-automation.Src.PageObject.Locators import Locator


class SearchResults(object):

    def __init__(self, driver):
        self.driver = driver
        # Results page locators definition
        self.sort_menu = driver.find_element(By.XPATH, Locator.sort_menu)
        self.review_hover_menu = driver.find_element(By.XPATH, Locator.review_hover_menu)
        self.create_list_link = driver.find_element(By.XPATH, Locator.create_list_link)

    # Sorting drop down menu
    def setSortingOrder(self, sort_order):
        select = Select(self.sort_menu)
        select.select_by_visible_text(sort_order)

    # ActionChains can be used in a chain pattern, in this case to hover over accounts menu and the clicking on a link
    def selectCreateList(self, driver):
        Hover = ActionChains(driver).move_to_element(self.review_hover_menu).move_to_element(self.create_list_link)
        Hover.click().perform()
