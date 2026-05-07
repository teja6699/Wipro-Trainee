from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Edge(service=Service('../resources/msedgedriver.exe'))
driver.maximize_window()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")
time.sleep(5 )

text_input = driver.find_element(By.ID, "my-text-id")
text_input.clear()
text_input.send_keys("Selenium Webdriver Demo")

password_input = driver.find_element(By.NAME,"my-password")
password_input.clear()
password_input.send_keys("secret123")

text_area = driver.find_element(By.NAME, "my-textarea")
text_area.clear()
text_area.send_keys("sample message")

checkbox= driver.find_element(By.ID, "my-check-2")


checkbox.click()

radio=driver.find_element(By.ID, "my-radio-2")


radio.click()

dropdown = driver.find_element(By.NAME, "my-select")
dropdown.click()
option = driver.find_element(By.CSS_SELECTOR, "select[name='my-select'] option[value='2']")
option.click()

multi_select = driver.find_element(By.NAME, "my-datalist")
multi_select.send_keys('Ney York')

file_upload = driver

time.sleep(5)
driver.quit()