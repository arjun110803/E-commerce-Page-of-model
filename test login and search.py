import time
from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.home_page import HomePage

def test_login_and_search():
    driver = get_driver()
    driver.get("https://example-ecommerce.com")

    login = LoginPage(driver)

    # Step 1: Verify landing page
    assert login.verify_login_page()
    print("Login page verified")

    # Step 2: Provide credentials
    login.enter_username("testuser")
    login.enter_password("password123")

    # Step 3: Click login
    login.click_login()

    # Step 4: Wait
    time.sleep(3)

    home = HomePage(driver)

    # Step 5: Verify home page
    assert home.verify_home_page()
    print("Home page verified")

    # Step 6: Search product
    home.search_product("Laptop")
    print("Product searched")

    driver.quit()
