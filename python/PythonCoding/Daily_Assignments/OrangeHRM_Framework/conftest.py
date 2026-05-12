import pytest

from selenium import webdriver
from selenium.webdriver.edge.service import Service

from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture()
def driver():

    driver = webdriver.Edge(
        service=Service(
            EdgeChromiumDriverManager().install()
        )
    )

    driver.maximize_window()

    driver.get(
        "https://opensource-demo.orangehrmlive.com/"
    )

    yield driver

    driver.quit()