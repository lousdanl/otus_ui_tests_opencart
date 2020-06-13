import allure
import pytest

from tests_opencart.locators import LocatorsMain as main
from tests_opencart.locators import LocatorsProduct as products
from tests_opencart.models.user import Main, Product

LIST_PRODUCTS = [main.IPHONE, main.CANONEOS5D]


@allure.severity(allure.severity_level.NORMAL)
def test_assert_elements(wd, open_main_page):
    main = Main(wd)
    main.select_product()
    product = Product(wd)
    product.find_elements()


@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("product_from_main", LIST_PRODUCTS)
def test_open_image(wd, open_main_page, product_from_main):
    main = Main(wd)
    main.select_product(product_from_main)
    product = Product(wd)
    image, number = product.open_image()
    product.switch_image(number)
    product.close_image()
    product.wait_staleness(image)


@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("product_from_main", LIST_PRODUCTS)
def test_add_to_cart(wd, open_main_page, product_from_main):
    main = Main(wd)
    main.select_product(product_from_main)
    product = Product(wd)
    products_name = product.get_products_name()
    product.select_option()
    product.add_to_cart()
    alert_text = product.alert_success()
    assert alert_text == products.ALERT_TEXT_TO_CART % products_name
