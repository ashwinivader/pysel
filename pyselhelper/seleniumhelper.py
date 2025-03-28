from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Selenium_Helper:
    def __init__(self, driver):
        self.driver=driver

    def webelement_click(self,locator)   : 
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator)).click()
        
    def webelement_enterText(self,locator,text)   : 
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(locator)).send_keys(text)   

    def webelement_get_text(self, locator):
        """Get the text of a web element after ensuring it is visible."""
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator)).text

    def webelement_is_displayed(self, locator):
        """Check if the element is visible on the page."""
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return element.is_displayed()
        except:
            print(f"Element located by {locator} is not visible.")
            return False

    def webelement_is_enabled(self, locator):
        """Check if the element is enabled (e.g., whether a button is clickable)."""
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator)).is_enabled()

    def webelement_get_attribute(self, locator, attribute):
        """Get the value of a specified attribute of the element."""
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator)).get_attribute(attribute) 

    def naviate_back(self):
        self.driver.back()
   