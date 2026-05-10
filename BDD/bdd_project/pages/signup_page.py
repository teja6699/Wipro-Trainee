from utils.logger import LogGen
from utils.waits import Waitutils
Logger LogGen.loggen ()
class SignupPage:
    def __init__(self, driver):
        self.driver = driver

    def click_signup_menu(self):
        Logger.info("Clicking Login Menu")
        WaitUtils.wait_for_element_clickable(self.driver,).click()