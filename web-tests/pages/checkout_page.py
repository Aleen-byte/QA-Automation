from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    FINISH_BTN = (By.ID, "finish")
    SUMMARY_TITLE = (By.CLASS_NAME, "title")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    COMPLETE_TEXT = (By.CLASS_NAME, "complete-text")

    def fill_info(self, first_name, last_name, postal_code):
        self.type(self.FIRST_NAME, first_name)
        self.type(self.LAST_NAME, last_name)
        self.type(self.POSTAL_CODE, postal_code)
        self.click(self.CONTINUE_BTN)
        self.wait.until(lambda d: "step-two" in d.current_url)

    def finish_order(self):
        self.click(self.FINISH_BTN)
        self.wait.until(lambda d: "complete" in d.current_url)

    def get_complete_header(self):
        return self.get_text(self.COMPLETE_HEADER)

    def get_summary_title(self):
        return self.get_text(self.SUMMARY_TITLE)
