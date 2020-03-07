from attributes.attribute_main import AttributeMainPage as main
from attributes.attribute_common import AttributeCommon as common


def test_assert_elements(driver):
    driver.find_element_by_link_text(common.YOUR_STORE).click()
    driver.find_element_by_css_selector(main.SLIDESHOW)
    driver.find_element_by_css_selector(main.CAROUSE)
    switch = driver.find_element_by_css_selector(main.SWITCH_ELEMENT)
    switch.find_element_by_css_selector(main.SWITCH)
    driver.find_element_by_css_selector(main.IN_CART % common.MACBOOK)
    driver.find_element_by_css_selector(main.IN_WISHLIST % common.IPHONE)
    driver.find_element_by_css_selector(main.IN_COMPARE % common.CANONEOS5D)
