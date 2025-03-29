import pytest
from conftest import base_url
from astmpages.HomePage import Homepage
import logging

@pytest.mark.usefixtures("browser_setup")
class TestHomepg:
    def setup_class(self):
        print("In setup")
        self.driver.get(base_url)
        self.homepg=Homepage(self.driver)
  
    def test_Logo(self):
        print("in testlogo")
        self.homepg.checkLogo()
        
    def test_Search(self):
        print("in test search icon")
        self.homepg.checksearch()
           
    def teardown_class(self):
        print("In tearrdown")
        self.driver.quit()       


