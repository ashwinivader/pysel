

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Set up the Chrome WebDriver using WebDriver Manager
driver = webdriver.Chrome()

# Open Google
driver.get("https://dev-www.astm.org/")

# Optional: Wait for a few seconds to see the browser (not required, just for demo purposes)
import time
time.sleep(5)

# Close the browser
driver.quit()


#driver.find_element()
"""
#function decorator
def my_decorator(fun):
  def wrapper():
    print("in side decorator")
    fun()
    print("out side decorator")
  return  wrapper  


@my_decorator
def fun1():
    print("AAA")

fun1()   
"""

#property decorator
"""
class prop:
    def __init__(self, amt):
        self.amount=amt

    @property
    def interest(self):
      return(self.amount*0.07)
    

p1=prop(100)   
print(p1.interest)     
"""
