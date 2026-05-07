import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import webDriverWait
import pytest check as check
@pytest.fixture(scope='function')
def driver():
    driver=webdriver.Edge()

    driver.maximize_window()

    driver.get('https://www.google.com')
    yield driver
    driver.quit()
def test_ghpload(driver):

    pagetitle = driver.title

    assert pagetitle == 'Google', 'Google Home Page Not Loaded'

def test_imagespageload(driver):
    driver.find_element(By.LINK_TEXT, 'Images').click()
    pagetitle=driver.title
    assert pagetitle == 'Google Images', 'Images pages Not Loaded'

def test_businesslink(driver):

    driver.find_element(By.LINK_TEXT, value: 'Business').click()

    wait = WebDriverWait(driver, timeout: 5)



    wait.until(EC.title_contains('Business'))
    assert 'Business' in driver.title, 'Business Page Not Loaded Title check'

    assert 'business' in driver.current_url, 'Business Page Not Loaded URL check