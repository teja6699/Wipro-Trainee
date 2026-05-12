from pages.login_page import LoginPage
from pages.pim_page import PIMPage


def test_employee_navigation(driver):

    login_page = LoginPage(driver)

    login_page.login(
        "Admin",
        "admin123"
    )

    driver.get(
        "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList"
    )

    pim_page = PIMPage(driver)

    details_page = pim_page.view_employee_details(
        "Paul Collings"
    )

    print(details_page.get_page_title())