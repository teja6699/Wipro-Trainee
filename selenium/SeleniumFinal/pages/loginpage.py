
from utils.loggersfrom selenium.webdriver.common.by import By
from pages.basepage import BasePage
from utils.loggers


class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        self.ERROR_MESSAGE = None

    def login(self, username="standard_user", password="secret_sauce"):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def read_error_message(self):
        """Returns the text of the error message displayed on the page."""
        return self.driver.find_element(*self.ERROR_MESSAGE).text