from selenium.webdriver.common.by import By


class AdminPage:

    usernames = (
        By.XPATH,
        "//div[@role='row']//div[2]"
    )

    def __init__(self, driver):

        self.driver = driver

    def is_user_present(self, username):

        users = self.driver.find_elements(
            *self.usernames
        )

        for user in users:

            if user.text.lower() == username.lower():

                return True

        return False