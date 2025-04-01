from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import logging
from selenium.webdriver.common.by import By
from datetime import datetime
from  pathlib import Path
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions

driver=None
base_url= "https://dev-www.astm.org/"


# Set up logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def pytest_addoption(parser):
    # Define the custom command-line option '--browser_type'
    parser.addoption(
        "--browser_type", action="store", default="chromium", help="Type of browser to use(chromium, webkit)"
    )



@pytest.fixture(scope="class",autouse=True)
def browser_setup(request):
    try:
        print("In browser setup")
        print(request)
        print(request.config.getoption("--browser_type"))
        logger.info("In browser setup")
        logger.info(f"Browser type: {request.config.getoption('--browser_type')}")
        browser_choice=request.config.getoption('--browser_type')
        if browser_choice.lower()=="chromium":
             #request.cls.driver=webdriver.Chrome()
            options = ChromeOptions()
            request.cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)
        elif browser_choice.lower()=="firefox":
             #request.cls.driver=webdriver.Firefox()
            options = FirefoxOptions()
            request.cls.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),options=options)
        elif browser_choice.lower() == "edge":
            edge_options = EdgeOptions()
            edge_options.use_chromium = True  # Ensure the Chromium-based Edge is used
            request.cls.driver = webdriver.Edge(
                service=EdgeService(EdgeChromiumDriverManager().install()),
                options=edge_options
            )   
        else:
           raise ValueError(f'Unsupported browser{browser_choice}')   
    except WebDriverException as e:
        logger.error(f"WebDriverException occurred: {e}")
        raise
    except Exception as e:
        logger.error(f"An error occurred during browser setup: {e}")
        raise
    else:
        logger.info(f"{browser_choice.capitalize()} browser initialized successfully.")
 
 


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
    logger.info(f"HTML report generated at {pytest_html}")


def pytest_html_report_title(report):
    report.title=" ASTM Test Teport"

    


# pytest -s --browser_type=chromium