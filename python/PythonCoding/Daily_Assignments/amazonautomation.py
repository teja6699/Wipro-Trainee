from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Launch Browser
driver = webdriver.Chrome()

# Implicit Wait
driver.implicitly_wait(10)

# Maximize Window
driver.maximize_window()

# Explicit Wait
wait = WebDriverWait(driver, 15)

try:

    # =========================================================
    # Exercise 1: Navigation and Title Verification
    # =========================================================

    driver.get("https://www.amazon.in")

    title = driver.title
    print("Page Title:", title)

    assert "Amazon" in title, "Title does not contain Amazon"

    # Navigate to Mobiles Page
    mobiles_link = driver.find_element(By.LINK_TEXT, "Mobiles")
    mobiles_link.click()

    print("Navigated to Mobiles Page")

    # Navigate Back
    driver.back()

    print("Returned to Home Page")



    # =========================================================
    # Exercise 2: Basic Locators and Search
    # =========================================================

    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.clear()
    search_box.send_keys("Wireless Headphones")

    search_button = driver.find_element(
        By.XPATH,
        "//input[@id='nav-search-submit-button']"
    )

    search_button.click()

    # Verify Search Results
    result_header = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(text(),'Wireless Headphones')]")
        )
    )

    assert result_header.is_displayed()

    print("Search Results Displayed Successfully")



    # =========================================================
    # Exercise 3: Implicit and Explicit Waits
    # =========================================================

    driver.back()

    laptop_search = driver.find_element(By.ID, "twotabsearchtextbox")
    laptop_search.clear()
    laptop_search.send_keys("Dell Inspiron Laptop")

    driver.find_element(
        By.ID,
        "nav-search-submit-button"
    ).click()

    # Wait for first product to appear
    first_product = wait.until(
        EC.visibility_of_element_located(
            (
                By.CSS_SELECTOR,
                "div.s-main-slot div[data-component-type='s-search-result']"
            )
        )
    )

    first_product.click()

    print("First Laptop Product Clicked")



    # =========================================================
    # Exercise 4: Advanced Locators
    # =========================================================

    driver.get("https://www.amazon.in")

    # Locate About Us using CSS Selector
    about_us = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a[href*='aboutamazon']")
        )
    )

    about_us.click()

    # Locate element using LINK_TEXT
    careers_link = wait.until(
        EC.visibility_of_element_located(
            (By.LINK_TEXT, "Careers")
        )
    )

    print("Element Text:", careers_link.text)



    # =========================================================
    # Exercise 5: Element Interaction and Synchronization
    # =========================================================

    driver.get("https://www.amazon.in")

    smart_watch_search = driver.find_element(
        By.ID,
        "twotabsearchtextbox"
    )

    smart_watch_search.clear()
    smart_watch_search.send_keys("Smart Watches")

    driver.find_element(
        By.ID,
        "nav-search-submit-button"
    ).click()

    # Click Samsung Brand Filter
    samsung_brand = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[text()='Samsung']")
        )
    )

    samsung_brand.click()

    # Wait for refreshed results
    wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "div.s-main-slot")
        )
    )

    # Count products
    products = driver.find_elements(
        By.CSS_SELECTOR,
        "div[data-component-type='s-search-result']"
    )

    print("Number of products displayed:", len(products))


except TimeoutException:
    print("Element took too much time to load")

except AssertionError as e:
    print("Assertion Error:", e)

except Exception as e:
    print("Exception occurred:", e)

finally:
    time.sleep(3)
    driver.quit()
    print("Browser Closed")