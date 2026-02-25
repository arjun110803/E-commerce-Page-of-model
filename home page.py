from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    search_box = (By.NAME, "search")
    home_banner = (By.XPATH, "//div[contains(text(),'Welcome')]")

    def verify_home_page(self):
        return self.driver.find_element(*self.home_banner).is_displayed()

    def search_product(self, product):
        self.driver.find_element(*self.search_box).send_keys(product)
