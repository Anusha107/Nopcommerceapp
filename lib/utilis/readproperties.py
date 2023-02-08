"""
    This module is used to read the data from the config.ini file
"""
import configparser

config=configparser.RawConfigParser()
config.read(r".\configuration\config.ini")
class ReadConfig():
    @staticmethod
    def get_applicationURL():
        return config.get('commoninfo','URL')
    @staticmethod    
    def get_screenshot_path():
        return config.get('commoninfo','SCREENSHOT_PATH')
    @staticmethod    
    def get_testdata_path():
        return config.get('commoninfo','TEST_DATA_PATH')    
    @staticmethod    
    def get_username():
        return config.get('credentails','username')
    @staticmethod    
    def get_password():
        return config.get('credentails','password')         
    
