from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Selenium_Helper:
    def __init__(self, driver):
        self.driver=driver

    """def webelement_click(self,locator)   : 
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator)).click()"""
    
    def webelement_click(self, locator):
    #Click on the element using Fluent Wait.
        try:
            # Define Fluent Wait with custom polling frequency (1 second) and ignoring exceptions like NoSuchElementException
            wait = WebDriverWait(self.driver, 10, poll_frequency=1, ignored_exceptions=[Exception])
            
            # Wait for the element to be visible and then click it
            element = wait.until(EC.visibility_of_element_located(locator))
            
            # Click the element
            element.click()
        except Exception as e:
            print(f"Unable to click the element located by {locator}. Exception: {str(e)}")
        
    """def webelement_enterText(self,locator,text)   : 
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(locator)).send_keys(text) """

    def webelement_enterText(self, locator, text):
    #Enter text into an input field using Fluent Wait.
        try:
            # Define Fluent Wait with custom polling frequency (1 second)
            wait = WebDriverWait(self.driver, 5, poll_frequency=1, ignored_exceptions=[Exception])
            
            # Wait for the element to be visible and then enter the text
            element = wait.until(EC.visibility_of_element_located(locator))
            
            # Clear the input field (optional, in case there is pre-existing text)
            element.clear()
            
            # Enter the provided text into the input field
            element.send_keys(text)
        except Exception as e:
            print(f"Unable to enter text into the element located by {locator}. Exception: {str(e)}") 

    """def webelement_get_text(self, locator):
        #Get the text of a web element after ensuring it is visible.
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator)).text"""
    
    def webelement_get_text(self, locator):
        #Get the text of a web element using Fluent Wait.
        try:
            # Define Fluent Wait with custom polling frequency (1 second)
            wait = WebDriverWait(self.driver, 5, poll_frequency=1, ignored_exceptions=[Exception])        
            # Wait for the element to be visible
            element = wait.until(EC.visibility_of_element_located(locator))         
            # Return the text of the element
            return element.text
        except Exception as e:
            print(f"Unable to get text from the element located by {locator}. Exception: {str(e)}")
            return None

    """def webelement_is_displayed(self, locator):
        #Check if the element is visible on the page.
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return element.is_displayed()
        except:
            print(f"Element located by {locator} is not visible.")
            return False"""
    
    def webelement_is_displayed(self, locator):
    #Check if the element is visible on the page using Fluent Wait.
        try:
            # Define Fluent Wait
            wait = WebDriverWait(self.driver, 10, poll_frequency=1, ignored_exceptions=[Exception])         
            # Wait for the visibility of the element with a fluent wait
            element = wait.until(EC.visibility_of_element_located(locator))         
            # Return whether the element is displayed
            return element.is_displayed()
        except Exception as e:
            print(f"Element located by {locator} is not visible. Exception: {str(e)}")
        return False

    """def webelement_is_enabled(self, locator):
        #Check if the element is enabled (e.g., whether a button is clickable).
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator)).is_enabled()"""
    
    def webelement_is_enabled(self, locator):
    #Check if the element is enabled (e.g., whether a button is clickable) using Fluent Wait.
        try:
            # Define Fluent Wait with custom polling frequency (1 second)
            wait = WebDriverWait(self.driver, 5, poll_frequency=1, ignored_exceptions=[Exception])
            
            # Wait for the element to be visible
            element = wait.until(EC.visibility_of_element_located(locator))
            
            # Return whether the element is enabled (clickable)
            return element.is_enabled()
        except Exception as e:
            print(f"Element located by {locator} is not enabled. Exception: {str(e)}")
            return False

    """def webelement_get_attribute(self, locator, attribute):
        #Get the value of a specified attribute of the element.
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator)).get_attribute(attribute)"""
    
    def webelement_get_attribute(self, locator, attribute):
        #Get the value of a specified attribute of the element using Fluent Wait.
        try:
            # Define Fluent Wait with custom polling frequency (1 second)
            wait = WebDriverWait(self.driver, 5, poll_frequency=1, ignored_exceptions=[Exception])
            
            # Wait for the element to be visible
            element = wait.until(EC.visibility_of_element_located(locator))
            
            # Return the value of the specified attribute
            return element.get_attribute(attribute)
        except Exception as e:
            print(f"Unable to get attribute '{attribute}' for element located by {locator}. Exception: {str(e)}")
            return None

    def naviate_back(self):
        self.driver.back()
   