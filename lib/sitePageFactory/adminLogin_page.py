"""
 This Module contains elements details of - Admin : Login Page
"""

from selenium.webdriver.common.by import By
from lib.utilis.base_page_object import BasePage
from selenium.common.exceptions import NoSuchElementException

class LoginPage(BasePage):
    def __init__(self, browser):
        BasePage.__init__(self, browser)
        self.browser = browser

    # Instance Variable
    locator_dictionary = {
        "username_textbox" : (By.ID, "Email"),
        "password_textbox" : (By.ID, "Password"),
        "login_button" : (By.XPATH, "//button[text()='Log in']"),
         "invalid_login_error_message":(By.XPATH, "//div[contains(text(),'Login was unsuccessful.')]")
    }

    def username_textbox(self):
        try:
            return self.browser.find_by_element_locator(LoginPage.locator_dictionary['username_textbox'])
        except NoSuchElementException:
            return None

    def password_textbox(self):
        try:
            return self.browser.find_by_element_locator(LoginPage.locator_dictionary['password_textbox'])
        except NoSuchElementException:
            return None

    def login_button(self):
        try:
            return self.browser.find_by_element_locator(LoginPage.locator_dictionary['login_button'])
        except NoSuchElementException:
            return None

    def invalid_login_error_message(self):
        try:
            return self.browser.find_by_element_locator(LoginPage.locator_dictionary['invalid_login_error_message'])
        except NoSuchElementException:
            return None