import pytest

from locators import LocatorsProduct as products
from locators import LocatorsMain as main
from models.user import Main, Product

LIST_PRODUCTS = [main.MAC,
                 main.IPHONE,
                 main.CANONEOS5D]


def test_assert_elemts(wd, open_main_page):
    main = Main(wd)
    product = Product(wd)
    main.select_product()
    product.find_elements()


@pytest.mark.parametrize('product_from_main', LIST_PRODUCTS)
def test_open_image(wd, open_main_page, product_from_main):
    main = Main(wd)
    product = Product(wd)
    main.select_product(product_from_main)
    image, number = product.open_image()
    product.switch_image(number)
    product.close_image()
    product.wait_staleness(image)


@pytest.mark.parametrize('product_from_main', LIST_PRODUCTS)
def test_add_to_cart(wd, open_main_page, product_from_main):
    main = Main(wd)
    product = Product(wd)
    main.select_product(product_from_main)
    products_name = product.get_products_name()
    product.select_option()
    product.add_to_cart()
    alert_text = product.alert_success()
    assert alert_text == products.ALERT_TEXT_TO_CART % products_name
