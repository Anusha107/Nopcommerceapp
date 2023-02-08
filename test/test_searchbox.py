import pytest,time
#from .conftest import SCREENSHOT_PATH
#from lib.sitePageFactory.adminLogin_page import LoginPage
from lib.sitePageFactory.amazonSearch_page import HomePage

#from lib.utilis.readproperties import ReadConfig
from lib.utilis.customLogger import LogGenerator



class Test_searchbox:
    logger = LogGenerator.loggen()

    def test_product(self,browser_assignment):
        HomePage(browser_assignment).search_textbox().clear()
        #HomePage(browser_assignment).password_textbox().clear()
        self.logger.info("***************** login_cred *****************")
        self.logger.info("***************** Test Case Started - login_cred *****************")

        # LoginPage(browser_assignment).username_textbox().send_keys("admin@yourstore.com")
        # LoginPage(browser_assignment).password_textbox().send_keys("admin")
        # LoginPage(browser_assignment).login_button().click()
        HomePage(browser_assignment).search_textbox().send_keys("iPhone XR (64GB) - Yellow.")
        time.sleep(2)