from attributes.attribute_category import AttributeCategory as category
from attributes.attribute_common import AttributeCommon as common


def test_asserts_elements(wd):
    wd.find_element_by_link_text(common.MENU_DESKTOPS).click()
    wd.find_element_by_link_text(common.SELECT_ALL_DESKTOPS).click()
    wd.find_element_by_css_selector(category.BREADCRUMB)
    wd.find_element_by_css_selector(category.SHOW_LIMIT)
    wd.find_element_by_css_selector(category.GRID)
    wd.find_element_by_css_selector(category.LIST)
    wd.find_element_by_css_selector(category.SORT)
