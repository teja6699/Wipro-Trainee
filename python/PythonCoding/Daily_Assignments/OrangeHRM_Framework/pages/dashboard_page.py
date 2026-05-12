from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:

    dashboard_heading = (
        By.XPATH,
        "//h6[text()='Dashboard']"
    )

    def __init__(self, driver):

        self.driver = driver

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                self.dashboard_heading
            )
        )

    def is_dashboard_displayed(self):

        return self.driver.find_element(
            *self.dashboard_heading
        ).is_displayed()