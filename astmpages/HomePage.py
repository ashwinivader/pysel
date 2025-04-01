from pyselhelper.seleniumhelper import Selenium_Helper
from selenium.webdriver.common.by import By


import pytest
from conftest import base_url
import logging


# Set up logger for the test class
logger = logging.getLogger(__name__)


class Homepage(Selenium_Helper):
    #locaptors of the home page
    astmLogo=(By.XPATH,"(//img[@alt='ASTM-newLogo'])[1]")
    searchicon=(By.XPATH,"(//input[@type='search'])[2]")
    


    def __init__(self,driver):
        super().__init__(driver)

    def checkLogo(self):
        print("Checking logo visibility...")
        logger.info("Running test_Logo")
        #print(Selenium_Helper.webelement_is_displayed(self.astmLogo))
        result=super().webelement_is_displayed(self.astmLogo)
        print(f"Logo is displayed: {result}")  # Output the result of the visibility check
        return result
    
    def checksearch(self):
        logger.info("Running test_Search")
        print("Checking search text visibility...")
        #print(Selenium_Helper.webelement_is_displayed(self.astmLogo))
        result=super().webelement_is_displayed(self.searchicon)
        print(f"search icon is displayed: {result}")  # Output the result of the visibility check
        return result




      


