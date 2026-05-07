import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
@pytest.fixture (scope="module")
def driver():
    driver webdriver. Edge()
    driver.maximize_window()
    driver.get("https://www.amazon.in")
    yield driver
    driver.quit()
I
#service-Service("../resources