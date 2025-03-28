from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import logging
from selenium.webdriver.common.by import By

driver=None
base_url= "http://dev-www.astm.org"



@pytest.fixture(scope="class",autouse=True)
def browser_setup(request):
    request.cls.driver=webdriver.Chrome()





