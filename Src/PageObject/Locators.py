__author__ = 'Enrique Cosio'

class Locator(object):

        # Home page
        logo = "//*[@id='nav-logo']"
        orders_link = "//a[contains(text(),'Orders')]"
        search_bar = "//*[@id='twotabsearchtextbox']"
        search_button = "nav-input"
        
        # Results page
        sort_menu = "//*[@id='sort']"
        review_hover_menu = "//*[@id='nav-link-accountList']"
        create_list_link = "//*[contains(text(),'Create a List')]"
        
