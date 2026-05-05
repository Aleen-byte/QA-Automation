import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

VALID_USER = "standard_user"
VALID_PASS = "secret_sauce"


class TestLogin:
    def test_login_valid_credentials(self, driver):
        login = LoginPage(driver)
        login.open()
        login.login(VALID_USER, VALID_PASS)

        inventory = InventoryPage(driver)
        assert inventory.get_title() == "Products"

    def test_login_invalid_credentials(self, driver):
        login = LoginPage(driver)
        login.open()
        login.login("wrong_user", "wrong_pass")

        assert "Username and password do not match" in login.get_error_message()

    def test_login_locked_user(self, driver):
        login = LoginPage(driver)
        login.open()
        login.login("locked_out_user", VALID_PASS)

        assert "locked out" in login.get_error_message().lower()


class TestCart:
    def test_add_single_item_to_cart(self, driver):
        login = LoginPage(driver)
        login.open()
        login.login(VALID_USER, VALID_PASS)

        inventory = InventoryPage(driver)
        inventory.add_item_to_cart(0)

        assert inventory.get_cart_count() == 1

    def test_add_multiple_items_to_cart(self, driver):
        login = LoginPage(driver)
        login.open()
        login.login(VALID_USER, VALID_PASS)

        inventory = InventoryPage(driver)
        inventory.add_items_to_cart([0, 1, 2])

        assert inventory.get_cart_count() == 3

    def test_cart_shows_added_items(self, driver):
        login = LoginPage(driver)
        login.open()
        login.login(VALID_USER, VALID_PASS)

        inventory = InventoryPage(driver)
        inventory.add_items_to_cart([0, 1])
        inventory.go_to_cart()

        cart = CartPage(driver)
        assert cart.get_title() == "Your Cart"
        assert cart.get_items_count() == 2


class TestCheckout:
    def test_complete_purchase_flow(self, driver):
        """Fluxo E2E completo: login → adicionar produtos → checkout → confirmação."""
        # Login
        login = LoginPage(driver)
        login.open()
        login.login(VALID_USER, VALID_PASS)

        # Adicionar produtos ao carrinho
        inventory = InventoryPage(driver)
        assert inventory.get_title() == "Products"
        inventory.add_items_to_cart([0, 1])
        assert inventory.get_cart_count() == 2
        inventory.go_to_cart()

        # Verificar carrinho
        cart = CartPage(driver)
        assert cart.get_items_count() == 2
        cart.proceed_to_checkout()

        # Preencher dados e finalizar
        checkout = CheckoutPage(driver)
        assert checkout.get_summary_title() == "Checkout: Your Information"
        checkout.fill_info("Théo", "Tester", "60000-000")

        assert checkout.get_summary_title() == "Checkout: Overview"
        checkout.finish_order()

        # Confirmar pedido
        assert checkout.get_complete_header() == "Thank you for your order!"
