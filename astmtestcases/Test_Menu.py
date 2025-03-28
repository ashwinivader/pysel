import pytest
from conftest import base_url
from astmpages.MenuPage import Menupage
import logging

@pytest.mark.usefixtures("browser_setup")
class TestMenu:
    def setup_class(self):
        print("In setup")
        self.driver.get(base_url)
        self.Menupg=Menupage(self.driver)
  

    def test_aboutMenu(self):
        print("in testlogo")
        self.Menupg.aboutAstm()

           
    def teardown_class(self):
        print("In tearrdown")
        self.driver.quit()       


