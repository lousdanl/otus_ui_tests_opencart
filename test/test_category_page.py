from attributes.attribute_category import AttributeCategory as category
from attributes.attribute_common import AttributeCommon as common


def test_asserts_elements(driver):
    driver.find_element_by_link_text(common.MENU_DESKTOPS).click()
    driver.find_element_by_link_text(common.SELECT_ALL_DESKTOPS).click()
    driver.find_element_by_css_selector(category.BREADCRUMB)
    driver.find_element_by_css_selector(category.SHOW_LIMIT)
    driver.find_element_by_css_selector(category.GRID)
    driver.find_element_by_css_selector(category.LIST)
    driver.find_element_by_css_selector(category.SORT)
