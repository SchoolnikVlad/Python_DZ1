import pytest
from selenium import webdriver
from LoginPage import LoginPage
from InventoryPage import InventoryPage
from CartPage import CartPage

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test(driver):
    login_page = LoginPage(driver)
    login_page.open()

    inventory_page = InventoryPage(driver)
    inventory_page.add_item_to_cart("Sauce Labs Backpack")
    inventory_page.add_item_to_cart("Sauce Labs Bolt T-Shirt")
    inventory_page.add_item_to_cart("Sauce Labs Onesie")

    inventory_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.checkout()

    cart_page.fill_out_form("John", "Doe", "12345")

    total_price = cart_page.get_total_price()
    assert total_price == "$58.29"

    cart_page.quit()