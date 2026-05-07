import time
from time import sleep

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.relative_locator import locate_with

driver = webdriver.Edge(service=Service('../resources/msedgedriver.exe'))  #(service = Service(EdgeChromiumDriverManager().install()))
driver.get("https://www.saucedemo.com")
#search_input = driver.find_element(By.ID, value="APjFqb")
#search_input.send_keys("selenium")


#search_input = driver.find_element(By.NAME, value="q")
#search_input.send_keys("locators")
#time.sleep(5)

#googlesearch_button = driver.find_element(By.NAME, value="btnK")
#googlesearch_button.click()
#time.sleep(200)
#search_input.clear()

#imfl_buttton = driver.find_element(By.CLASS_NAME, value="RNmpXc")
#imfl_buttton.click()
#sleep(5)

"""
href_button = driver.find_elements(By.TAG_NAME, value='a')
for ele in href_button:
    print(f'{ele.text} - {ele.get_attribute("href")}')
"""
#images_linl = driver.find_element(By.LINK_TEXT, value="Images")
#images_linl.click()
#sleep(5)

#images_linl = driver.find_element(By.PARTIAL_LINK_TEXT, value="Ima")
#images_linl.click()
#sleep(5)

#search_input = driver.find_element(By.CSS_SELECTOR, value='div> textarea')
#search_input.send_keys("selenium")
#time.sleep(5)
#setting_text = driver.find_element(By.XPATH, value='/html/body/div[2]/div[7]/div/div[2]/div[2]/span/span/g-popup/div/div')
#print(setting_text.text)
sleep(5)
#[and_ex = driver.find_element(By.XPATH, value="//td[text()='Tim' and @class='first-name']")

#print(f"And Ex -> Found with both conditions: {and_ex.text}")
#or_ex = driver.find_element(By.XP"//td[text()='Tim' or text()='Frank']")
#print(f"Anor -> Found with or conditions: {or_ex.text}")

#rows=driver.find_elements(By.XPATH, "//table[@id='table1']/tbody/tr/td")
#print(f"Child Example -> Found {len(rows)} columns in the first table.")

#email_cell = driver.find_element(By.XPATH, "//table@id='table1']//td[text()='jdoe@hotmail.com]")
#parent_row = driver.find_element(By.XPATH, "//table@id='table1']//td[text()='jdoe@hotmail.com]/parent::tr")
#print(f"Parent Example -> Email '{email_cell.text}' belongs to row with first name: "
 #     f"{parent_row.find_elements(By.XPATH,'./td[2]').text}")
 #
#ancestor_table = driver.find_element(By.XPATH, "//td[text()='jsmith@gmail.com']/ancestor::table")
#print(f"Ancestor Example -> Table ID: {ancestor_table.get_attribute('id')}")
##descendants = driver.find_element(By.XPATH, "//table[@id = 'table1']/descendant::td")
#print(f"Descendant Example -> Found {len(descendants)} descandant cells. ")
 

username_field= driver.find_element(By.ID, "user-name")
password_field= driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

elmt_above_password = driver.find_element(
    locate_with(By.TAG_NAME, "input").above(password_field)
)
print(f"Above Example Text above password: {elmt_above_password.get_attribute('placeholder')}")

elmt_above_password.send_keys('standard_user')


time.sleep(5)
field_below_username = driver.find_element(locate_with(By.TAG_NAME, "input").below (username_field)
)
print(f"Below Example Placeholder below username: {field_below_username.get_attribute('placeholder')}")

field_below_username.send_keys('secret_sauce')

time.sleep(2)
#above element located above another  elmt_above_password = driver.find_element

twitter_icon = driver.find_element(By.LINK_TEXT, "Twitter")




facebook_icon = driver.find_element(locate_with(By.TAG_NAME,  "a").to_right_of(twitter_icon))

print(f"toRightof Example Element to the right of Twitter icon has href: {facebook_icon.get_attribute('href')}")

left_icon = driver.find_element(locate_with(By.TAG_NAME, "a").to_left_of(facebook_icon))


print(f"toLeftof Example Element to the left of Facebook icon has href: {left_icon.get_attribute('href')}")

near_twitter = driver.find_elements(locate_with(By.TAG_NAME,  "a").near(facebook_icon))
for element in near_twitter:
    print(f"Near Example Element near Facebook icon has href: {element.get_attribute('href')}")
tiBy.LINK_TEXTdriver.quit()