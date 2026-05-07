
from pages.home_page import HomePage
from pages.product_listing_page import ProductListingPage


def test_open_amazon(driver):
    assert "amazon" in driver.current_url, 'URL for amazon is not correct'
    print("\nOpened Amazon Homepage. Title & URL verified.")
def test_search_product(driver):
    homepage=HomePage(driver)

    homepage.type_search_input()
    homepage.click_search_button()

    assert homepage.is_amazon_page_loaded() == True, 'Search results page did not load.'
    print("\nSearch results page loaded successfully.")

def test_find_elements_amazon(driver):
    productlistingpage = ProductListingPage(driver)

    productlistingpage.find_product_title()
    val = productlistingpage.all_products()