from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class InventoryPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    ITEMS = (By.CLASS_NAME, "inventory_item")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def get_title(self):
        return self.get_text(self.TITLE)

    def add_item_to_cart(self, item_index=0):
        """Adiciona um item ao carrinho pelo índice e aguarda o badge atualizar."""
        self.wait.until(EC.presence_of_all_elements_located(self.ITEMS))
        current_count = self.get_cart_count()
        self.driver.execute_script(
            "document.querySelectorAll('.inventory_item')[arguments[0]]"
            ".querySelector('button.btn_inventory').click();",
            item_index
        )
        self.wait.until(lambda d: self.get_cart_count() == current_count + 1)

    def add_items_to_cart(self, indexes):
        for i in indexes:
            self.add_item_to_cart(i)

    def get_cart_count(self):
        badges = self.driver.find_elements(*self.CART_BADGE)
        return int(badges[0].text) if badges else 0

    def go_to_cart(self):
        self.driver.get("https://www.saucedemo.com/cart.html")
