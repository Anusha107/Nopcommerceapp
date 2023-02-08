import pytest
#from .conftest import SCREENSHOT_PATH
from lib.sitePageFactory.adminLogin_page import LoginPage
from lib.sitePageFactory.home_page import HomePage

from lib.utilis.readproperties import ReadConfig
from lib.utilis.customLogger import LogGenerator
from lib.utilis import excelutil



class Test_Login:
    logger = LogGenerator.loggen()
    test_data_path= ReadConfig.get_testdata_path()
    

    def test_loginPageTitle(self, browser_assignment):
        self.logger.info("***************** loginPageTitle *****************")
        self.logger.info("***************** Test Case Started - loginPageTitle *****************")
        fetched_tilte = browser_assignment.get_title()
        print("Fetched Title:", fetched_tilte)

        if fetched_tilte == "Your store. Login":
            assert True
            self.logger.info("***************** Test Case Status - Passed *****************")
        else:
            browser_assignment.get_screenshot(ReadConfig.get_screenshot_path() + 'test_loginPageTitle.png')
            self.logger.error("***************** Test Case Status - Failed *****************")
            assert False
            

    def test_login_cred(self, browser_assignment):
        
        self.logger.info("***************** login_cred *****************")
        self.logger.info("***************** Test Case Started - login_cred *****************")
        self.number_of_rows=excelutil.get_Rowcount(self.test_data_path,'Sheet1')
        self.number_of_columns=excelutil.get_Columncount(self.test_data_path,'Sheet1')
        print("number of rows:{} and number of columns:{}".format(self.number_of_rows,self.number_of_columns))
        for val in range(2,self.number_of_rows+1):
            self.username=excelutil.read_data(filename=self.test_data_path,sheetname='Sheet1',rowNumber=val,coloumnNumber=1)
            self.password=excelutil.read_data(filename=self.test_data_path,sheetname='Sheet1',rowNumber=val,coloumnNumber=2)
            print("username:{},password:{}".format(self.username,self.password))

            LoginPage(browser_assignment).username_textbox().clear()
            LoginPage(browser_assignment).password_textbox().clear()

            LoginPage(browser_assignment).username_textbox().send_keys(self.username)
            LoginPage(browser_assignment).password_textbox().send_keys(self.password)

            LoginPage(browser_assignment).login_button().click()

            fetched_title = browser_assignment.get_title()

            if fetched_title == "Dashboard / nopCommerce administration":
                assert True
                self.logger.info("***************** Test Case Status - Passed *****************")
                HomePage(browser_assignment).logout_button().click()
            else:
                browser_assignment.get_screenshot(ReadConfig.get_screenshot_path()  + 'test_login_cred.png')
                
                error_message=LoginPage(browser_assignment).invalid_login_error_message().text
                print("Error_message",error_message)
                if error_message=="Login was unsuccessful. Please correct the errors and try again.":
                   assert True
                   self.logger.info("***************** Test Case Status - passed for invalid credentials *****************")
                 
    
                 