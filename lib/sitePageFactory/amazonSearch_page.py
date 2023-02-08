from selenium.webdriver.common.by import By
from lib.utilis.base_page_object import BasePage
from selenium.common.exceptions import NoSuchElementException

class HomePage(BasePage):
    def __init__(self, browser):
        BasePage.__init__(self, browser)
        self.browser = browser

    # Instance Variable
    locator_dictionary = {
        "search_textbox" : (By.ID, "twotabsearchtextbox"),
        # "catalogue_button":(By.XPATH, "//i[@class='nav-icon fas fa-book']"),
    }

    def search_textbox(self):

        try:
            return self.browser.find_by_element_locator(HomePage.locator_dictionary['search_textbox'])
        except NoSuchElementException:
            return None
    # def catalogue_button(self):
    #     try:
    #         return self.browser.find_by_element_locator(HomePage.locator_dictionary['catalogue_button'])
    #     except NoSuchElementException:
    #         return None           
         

    