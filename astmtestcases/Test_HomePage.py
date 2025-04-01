import pytest
from conftest import base_url
from astmpages.HomePage import Homepage
import logging

# Set up logger for the Homepage class
logger = logging.getLogger(__name__)

@pytest.mark.usefixtures("browser_setup")
class TestHomepg:
    def setup_class(self):
        print("In setup")
        self.driver.get(base_url)
        self.homepg=Homepage(self.driver)
  
    def test_Logo(self):
        logger.info("Checking logo visibility...")
        print("in testlogo")
        if self.homepg.checkLogo():
          logger.info("ASTM logo is displayed on the homepage.")
        else:
          logger.info("ASTM logo is not displayed on the homepage.")

        
    def test_Search(self):
        print("in test search icon")
        logger.info("Checking search icon visibility...")
        if self.homepg.checksearch():
          logger.info("Search icon is displayed on the homepage.")
        else:
          logger.info("Search icon is not displayed on the homepage.")
           
    def teardown_class(self):
        logger.info("In teardown...")
        print("In tearrdown")
        self.driver.quit()       


