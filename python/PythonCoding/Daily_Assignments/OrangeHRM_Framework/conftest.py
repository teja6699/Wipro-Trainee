import pytest

from selenium import webdriver

from selenium.webdriver.edge.service import Service


@pytest.fixture()
def driver():

    service = Service(
        executable_path=r"C:\softwares\edgedriver_win64\msedgedriver.exe"
    )

    driver = webdriver.Edge(service=service)

    driver.maximize_window()

    driver.implicitly_wait(10)

    driver.get(
        "https://opensource-demo.orangehrmlive.com/"
    )

    yield driver

    driver.quit()