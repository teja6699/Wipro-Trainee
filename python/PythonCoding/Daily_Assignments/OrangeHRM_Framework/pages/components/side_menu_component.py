from selenium.webdriver.common.by import By


class SideMenuComponent:

    admin_menu = (By.XPATH, "//span[text()='Admin']")
    pim_menu = (By.XPATH, "//span[text()='PIM']")
    leave_menu = (By.XPATH, "//span[text()='Leave']")
    search_input = (
        By.XPATH,
        "//input[@placeholder='Search']"
    )

    def __init__(self, driver):

        self.driver = driver

    def click_admin(self):

        self.driver.find_element(
            *self.admin_menu
        ).click()

    def click_pim(self):

        self.driver.find_element(
            *self.pim_menu
        ).click()

    def click_leave(self):

        self.driver.find_element(
            *self.leave_menu
        ).click()

    def search_menu(self, menu_name):

        self.driver.find_element(
            *self.search_input
        ).send_keys(menu_name)