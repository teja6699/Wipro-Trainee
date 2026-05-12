import pytest

from pages.login_page import LoginPage
from pages.admin_page import AdminPage


@pytest.mark.parametrize(
    "username",
    [
        "Admin",
        "Paul",
        "TestingUser"
    ]
)
def test_verify_user_exists(driver, username):

    login_page = LoginPage(driver)

    login_page.login(
        "Admin",
        "admin123"
    )

    driver.get(
        "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers"
    )

    admin_page = AdminPage(driver)

    result = admin_page.is_user_present(username)

    print(f"{username} : {result}")

    assert result