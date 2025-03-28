
import pytest
from conftest import base_url
from selenium.webdriver.common.by import By
from pyselhelper.seleniumhelper import Selenium_Helper
import time


class Menupage(Selenium_Helper):
    #locaptors of the home page
    AboutAstm=(By.XPATH,"(//button[contains(text(),'About ASTM ')])[2]/i")
    MenuBar=(By.XPATH,"(//nav[@class,'main-nav-desktop navbar navbar-expand-md p-0 main-nav navbar-dark astm-navbar ms-auto overflow-auto'])[1]")
    AstmOverviewMenu=(By.XPATH,"(//h6//a[contains(text(),'About ASTM Overview')])[2]")
    governanceMenu=(By.XPATH,"(//div[@class='d-none d-md-block']//a[@title='Governance' and @class='nav-link header-navigation_subNavigation__G0vzo'])[2]")
    GlobalCooperationMenu=(By.XPATH,"(//div[@class='d-none d-md-block']//a[@title='Global Cooperation' and @class='nav-link header-navigation_subNavigation__G0vzo'])[2]")
    CorporateCitizenshipMenu=(By.XPATH,"(//div[@class='d-none d-md-block']//a[@title='Corporate Citizenship' and @class='nav-link header-navigation_subNavigation__G0vzo'])[4]")
    cookiepopup=(By.XPATH,"//button[@class='onetrust-close-btn-handler onetrust-close-btn-ui banner-close-button ot-close-icon']")    

    
    def __init__(self,driver):
        super().__init__(driver)

    def aboutAstm(self):
        print("Checking astm menu ...")
        #print(Selenium_Helper.webelement_is_displayed(self.astmLogo))
        time.sleep(2)
        super().webelement_click(self.cookiepopup)
        time.sleep(2)
        super().webelement_click(self.AboutAstm)
        time.sleep(2)
        super().webelement_click(self.AstmOverviewMenu)
        time.sleep(2)
        super().webelement_click(self.AboutAstm)
        time.sleep(2)
        super().webelement_click(self.governanceMenu)
        time.sleep(2)
        super().webelement_click(self.AboutAstm)
        time.sleep(2)
        super().webelement_click(self.GlobalCooperationMenu)
        time.sleep(2)
        super().webelement_click(self.AboutAstm)
        time.sleep(2)
        super().webelement_click(self.CorporateCitizenshipMenu)




    





      


