from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from pages.dashboard_page import DashboardPage


class LoginPage:

    username_input = (By.NAME, "username")

    password_input = (By.NAME, "password")

    login_button = (
        By.XPATH,
        "//button[@type='submit']"
    )

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 20)

    def login(self, username, password):

        self.wait.until(
            EC.visibility_of_element_located(
                self.username_input
            )
        )

        self.driver.find_element(
            *self.username_input
        ).send_keys(username)

        self.driver.find_element(
            *self.password_input
        ).send_keys(password)

        self.driver.find_element(
            *self.login_button
        ).click()

        return DashboardPage(self.driver)