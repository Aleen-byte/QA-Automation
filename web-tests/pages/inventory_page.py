from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    ITEMS = (By.CLASS_NAME, "inventory_item")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def get_title(self):
        return self.get_text(self.TITLE)

    def add_item_to_cart(self, item_index=0):
        """Adiciona um item ao carrinho pelo índice e aguarda o DOM confirmar."""
        items = self.driver.find_elements(*self.ITEMS)
        item = items[item_index]
        btn = item.find_element(By.CSS_SELECTOR, "button.btn_inventory")
        btn.click()
        self.wait.until(
            lambda d: item.find_element(By.CSS_SELECTOR, "button.btn_inventory").text == "Remove"
        )

    def add_items_to_cart(self, indexes):
        for i in indexes:
            self.add_item_to_cart(i)

    def get_cart_count(self):
        badges = self.driver.find_elements(*self.CART_BADGE)
        return int(badges[0].text) if badges else 0

    def go_to_cart(self):
        self.click(self.CART_LINK)
        self.wait.until(lambda d: "cart" in d.current_url)
