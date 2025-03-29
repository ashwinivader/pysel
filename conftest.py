from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import logging
from selenium.webdriver.common.by import By
from datetime import datetime
from  pathlib import Path

driver=None
base_url= "https://dev-www.astm.org/"

def pytest_addoption(parser):
    # Define the custom command-line option '--browser_type'
    parser.addoption(
        "--browser_type", action="store", default="chromium", help="Type of browser to use(chromium, webkit)"
    )

@pytest.fixture(scope="class",autouse=True)
def browser_setup(request):
    print("In browser setup")
    print(request)
    print(request.config.getoption("--browser_type"))
    request.cls.driver=webdriver.Chrome()
 


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # Get the current date and time
    today = datetime.now()   
    # Create the report directory (e.g., astmreports/20250329)
    report_dir = Path("astmreports", today.strftime("%Y%m%d"))
    report_dir.mkdir(parents=True, exist_ok=True)  # Create the directory if it doesn't exist 
    # Create the report file path with the current date and time (e.g., Report_202503291200.html)
    pytest_html = report_dir / f"Report_{today.strftime('%Y%m%d%H%M')}.html"
    # Configure pytest to use the generated HTML file for reports
    config.option.htmlpath = str(pytest_html)  # Set the path for the HTML report
    config.option.self_contained_html = True  # Embed the static assets in the HTML report


def pytest_html_report_title(report):
    report.title=" ASTM Test Teport"

    


