from selenium.webdriver.common.by import By
from pages.base_page import BasePage

URL = "https://www.saucedemo.com/"


class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR_MSG = (By.CSS_SELECTOR, "[data-test='error']")

    def open(self):
        self.driver.get(URL)

    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)
        self.wait.until(lambda d: d.current_url != URL)

    def get_error_message(self):
        return self.get_text(self.ERROR_MSG)
