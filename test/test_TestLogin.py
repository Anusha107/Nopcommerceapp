import pytest,time
#from .conftest import SCREENSHOT_PATH
from lib.sitePageFactory.adminLogin_page import LoginPage
from lib.sitePageFactory.home_page import HomePage

#from lib.utilis.readproperties import ReadConfig
from lib.utilis.customLogger import LogGenerator



class Test_Login:
    logger = LogGenerator.loggen()

    # def test_loginPageTitle(self, browser_assignment):
    #     self.logger.info("***************** loginPageTitle *****************")
    #     self.logger.info("***************** Test Case Started - loginPageTitle *****************")
    #     fetched_tilte = browser_assignment.get_title()
    #     print("Fetched Title:", fetched_tilte)

    #     if fetched_tilte == "Your store. Login":
    #         assert True
    #         self.logger.info("***************** Test Case Status - Passed *****************")
    #     else:
    #         browser_assignment.get_screenshot(ReadConfig.get_screenshot_path() + 'test_loginPageTitle.png')
    #         self.logger.error("***************** Test Case Status - Failed *****************")
    #         assert False
            

    # def test_login_cred(self, browser_assignment):
    #     LoginPage(browser_assignment).username_textbox().clear()
    #     LoginPage(browser_assignment).password_textbox().clear()
    #     self.logger.info("***************** login_cred *****************")
    #     self.logger.info("***************** Test Case Started - login_cred *****************")

    #     LoginPage(browser_assignment).username_textbox().send_keys(ReadConfig.get_username())
    #     LoginPage(browser_assignment).password_textbox().send_keys(ReadConfig.get_password())

    #     LoginPage(browser_assignment).login_button().click()

    #     fetched_title = browser_assignment.get_title()

    #     if fetched_title == "Dashboard / nopCommerce administration":
    #         assert True
    #         self.logger.info("***************** Test Case Status - Passed *****************")
    #     else:
    #         browser_assignment.get_screenshot(ReadConfig.get_screenshot_path()  + 'test_login_cred.png')
    #         self.logger.error("***************** Test Case Status - Failed *****************")
    #         assert False 
    def test_product(self,browser_assignment):
        LoginPage(browser_assignment).username_textbox().clear()
        LoginPage(browser_assignment).password_textbox().clear()
        self.logger.info("***************** login_cred *****************")
        self.logger.info("***************** Test Case Started - login_cred *****************")

        LoginPage(browser_assignment).username_textbox().send_keys("admin@yourstore.com")
        LoginPage(browser_assignment).password_textbox().send_keys("admin")
        LoginPage(browser_assignment).login_button().click()
        HomePage(browser_assignment).catalogue_button().click()
        time.sleep(2)

       