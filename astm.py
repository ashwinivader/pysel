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