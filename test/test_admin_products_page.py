import pytest
import allure

from models.admin import AdminProducts, AdminCommon, AdminSession
from db.check_data import CheckData

PRODUCT = [5]
IMAGE = ['test_image.jpg']


@allure.severity(allure.severity_level.NORMAL)
def test_assert_elements(wd, open_admin_page):
    admin = AdminSession(wd)
    admin.find_elements()
    assert admin.logs_have_errors()


@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize('image', IMAGE)
def test_add_new_product(db, wd, login, image):
    check = CheckData(db)
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
    assert product_model == check.find_last_product()
    assert admin.logs_have_errors()


@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize('product_number', PRODUCT)
def test_edit_product(db, wd, login, product_number):
    check = CheckData(db)
    admin_common = AdminCommon(wd)
    admin_common.open_catalog_products()
    admin = AdminProducts(wd)
    one_product = admin.get_one_product(product_number)
    product_id = admin.get_product_id_from_page(one_product)
    price = admin.product_price(one_product)
    admin.click_edit_product(one_product)
    new_price = admin.edit_price(price)
    admin.click_save_changes()
    admin.wait_alert_success()
    one_product = admin.get_one_product(product_number)
    price_from_page = admin.product_price(one_product)
    new_price_from_db = check.find_product_new_price(product_id)
    assert new_price == price_from_page
    assert new_price == new_price_from_db
    assert admin.logs_have_errors()


@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize('product_number', PRODUCT)
def test_delete_product(db, wd, login, product_number):
    check = CheckData(db)
    admin_common = AdminCommon(wd)
    admin_common.open_catalog_products()
    admin = AdminProducts(wd)
    first_product = admin.get_one_product(product_number)
    product_name = admin.get_product_name(first_product)
    admin.select_product(first_product)
    admin.click_button_copy()
    admin.wait_alert_success()
    count = admin.count_same_products(product_name)
    assert admin.assert_count_same_products(count)
    second_product = admin.get_one_product(product_number + 1)
    admin.get_product_id_from_page(second_product)
    product_id = admin.get_product_id_from_page(second_product)
    max_product_id = check.get_max_product_id()
    assert int(product_id) == max_product_id
    product_name = admin.get_product_name(second_product)
    admin.select_product(second_product)
    admin.click_button_delete()
    admin.accept_web_alert()
    admin.wait_alert_success()
    count = admin.count_same_products(product_name)
    max_id = check.get_max_product_id()
    assert product_id > max_id
    assert admin.assert_count_same_products(count) is False
    assert admin.logs_have_errors()


def test_product_delete(db, wd, login, file_new_product):
    check = CheckData(db)
    admin_common = AdminCommon(wd)
    admin_common.open_catalog_products()
    admin = AdminProducts(wd)

    product_name, product_model, date_available, date_added = admin.data_for_new_product()

    check.insert_new_product(
        file_new_product, product_model, date_available, date_added, date_added)
    product_id = check.get_max_product_id()
    check.insert_new_product_description(
        file_new_product, product_id, product_name, product_name)

    product = admin.find_product_by_id(product_id)
    admin.select_product(product)
    admin.click_button_delete()
    admin.accept_web_alert()
    admin.wait_alert_success()
    max_id = check.get_max_product_id()
    assert product_id > max_id





