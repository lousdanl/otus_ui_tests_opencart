from attributes.attribute_common import AttributeCommon as common
from attributes.attribute_product import AttributeProduct as product


def test_assert_elemts(driver):
    driver.find_element_by_css_selector(common.PRODUCT_MAC).click()
    driver.find_elements_by_css_selector(product.PRICE)
    driver.find_element_by_css_selector(product.QUANTITY)
    driver.find_element_by_css_selector(product.IN_CART)
    driver.find_element_by_css_selector(product.TAG_DESCRIPTION)
    driver.find_element_by_css_selector(product.TAG_REVIEWS)
