from time import sleep

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
"""
code for google home page
"""
driver = webdriver.Edge(service=Service('../resources/msedgedriver.exe'))  #(service = Service(EdgeChromiumDriverManager().install()))
driver.get("https://www.google.com")


pagetitle = driver.title
if pagetitle == "Google":
    print("Passed")
else:
    print("Failed")
sleep(2)

driver.quit()