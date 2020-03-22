from attributes.attribute_main import AttributeMain as main
from attributes.attribute_common import AttributeCommon as common


def test_assert_elements(wd, open_main_page):
    wd.find_element_by_css_selector(main.SLIDESHOW)
    wd.find_element_by_css_selector(main.CAROUSE)
    switch = wd.find_element_by_css_selector(main.SWITCH_ELEMENT)
    switch.find_element_by_css_selector(main.SWITCH)
    wd.find_element_by_css_selector(main.IN_CART % common.ID_MACBOOK)
    wd.find_element_by_css_selector(main.IN_WISHLIST % common.ID_IPHONE)
    wd.find_element_by_css_selector(main.IN_COMPARE % common.ID_CANONEOS5D)
