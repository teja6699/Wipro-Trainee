import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.wait import webDriverWait





@pytest.fixture (scope='module')

def test_multiple_windows_handle(driver):

    wait=WebDriverWait(driver, 10)
    parent_window=driver.current_window_handle
    driver.find_element(By.LINK_TEXT, "Click Here").click()
    time.sleep(3)


    all_windows=driver.window_handles
    assert len(all_windows) == 2, 'New Window did not open'
    for cwindow in all_windows:
        if cwindow != parent_window:
            driver.switch_to.window(cwindow)
            time.sleep(3)
            break

    time.sleep(3)
    header=wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h3"))).text
    assert header == "New Window", 'New Window switch did not happen'
    time.sleep(3)
    driver.close()
    driver.switch_to.window(parent_window)
    time.sleep(3)
    assert driver.title == "The Internet", 'Parent Window switch did not happen'

