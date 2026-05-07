from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductListingPage:

    PRODUCT_TITLES = (By.CSS_SELECTOR, "a h2 span")
    def __init__(self, driver):
        self.driver = driver
        self.waitWebDriverWait(self.driver,  10)

    def find_product_title(self):
        first_product self.wait.until( EC.visibility_of_element_located(self.PRODUCT_TITLES) )
        print("\nFirst Product:", first_product.text)
I
    def all_products (self, driver):
        product_titles = self.wait.until( EC.presence_of_all_elements_located (self.PRODUCT_TITLES) )
        print(f"\nFound (len(product_titles)} product titles on page one.\n")

        for i, title in enumerate (product_titles[:5], start=1):
            print(f"{i}. {title.text}")

        return len(product_titles) > 0
