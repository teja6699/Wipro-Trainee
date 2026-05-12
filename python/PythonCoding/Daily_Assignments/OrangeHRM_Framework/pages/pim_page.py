from selenium.webdriver.common.by import By
from pages.personal_details_page import PersonalDetailsPage


class PIMPage:

    employee_names = (
        By.XPATH,
        "//div[@role='row']//div[3]"
    )

    def __init__(self, driver):

        self.driver = driver

    def view_employee_details(self, employee_name):

        employees = self.driver.find_elements(
            *self.employee_names
        )

        for employee in employees:

            if employee.text == employee_name:

                employee.click()
                break

        return PersonalDetailsPage(self.driver)