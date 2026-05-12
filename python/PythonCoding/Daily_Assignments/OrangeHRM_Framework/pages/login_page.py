from selenium.webdriver.common.by import By
from pages.dashboard_page import DashboardPage


class LoginPage:

    username_input = (By.NAME, "username")
    password_input = (By.NAME, "password")
    login_button = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):

        self.driver = driver

    def login(self, username, password):

        self.driver.find_element(*self.username_input).send_keys(username)

        self.driver.find_element(*self.password_input).send_keys(password)

        self.driver.find_element(*self.login_button).click()

        return DashboardPage(self.driverpages)