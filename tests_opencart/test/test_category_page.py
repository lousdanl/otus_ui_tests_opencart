import allure

from tests_opencart.models.user import Category, Common


@allure.severity(allure.severity_level.NORMAL)
def test_asserts_elements(wd, open_main_page):
    common = Common(wd)
    common.menu_all_desktops()
    category = Category(wd)
    category.find_elements()
