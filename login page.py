from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    username = (By.ID, "username")
    password = (By.ID, "password")
    login_button = (By.ID, "loginBtn")
    login_text = (By.XPATH, "//h1[text()='Login']")

    # Actions
    def verify_login_page(self):
        return self.driver.find_element(*self.login_text).is_displayed()

    def enter_username(self, user):
        self.driver.find_element(*self.username).send_keys(user)

    def enter_password(self, pwd):
        self.driver.find_element(*self.password).send_keys(pwd)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()
