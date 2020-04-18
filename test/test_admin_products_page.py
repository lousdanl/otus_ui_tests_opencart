import pytest

from models.admin import AdminProducts, AdminCommon, AdminSession

PRODUCT = [0, 10]
IMAGE = ['test_image.jpg']


def test_assert_elements(wd, open_admin_page):
    admin = AdminSession(wd)
    admin.find_elements()
    assert admin.logs_have_errors()


@pytest.mark.parametrize('image', IMAGE)
def test_add_new_product(wd, login, image):
    common = AdminCommon(wd)
    common.open_catalog_products()
    admin = AdminProducts(wd)
    product_name, product_model = admin.product_data()
    admin.click_new_product()
    admin.assert_validation_add_form()
    admin.fill_general(product_name)
    admin.fill_data(product_model)
    admin.added_image(image)
    admin.click_save_changes()
    products = admin.get_name_all_products()
    assert product_name in products
    assert admin.logs_have_errors()


@pytest.mark.parametrize('product_number', PRODUCT)
def test_edit_product(wd, login, product_number):
    common = AdminCommon(wd)
    common.open_catalog_products()
    admin = AdminProducts(wd)
    one_product = admin.get_one_product(product_number)
    price = admin.product_price(one_product)
    admin.click_edit_product(one_product)
    new_price = admin.edit_price(price)
    admin.click_save_changes()
    admin.wait_alert_success()
    one_product = admin.get_one_product(product_number)
    price_from_page = admin.product_price(one_product)
    assert new_price == price_from_page
    assert admin.logs_have_errors()


@pytest.mark.parametrize('product_number', PRODUCT)
def test_delete_product(wd, login, product_number):
    common = AdminCommon(wd)
    common.open_catalog_products()
    admin = AdminProducts(wd)
    first_product = admin.get_one_product(product_number)
    product_name = admin.select_product(first_product)
    admin.click_button_copy()
    admin.wait_alert_success()
    count = admin.count_same_products(product_name)
    assert admin.assert_count_same_products(count)
    second_product = admin.get_one_product(product_number + 1)
    product_name = admin.select_product(second_product)
    admin.click_button_delete()
    admin.accept_web_alert()
    admin.wait_alert_success()
    count = admin.count_same_products(product_name)
    assert admin.assert_count_same_products(count) is False
    assert admin.logs_have_errors()
