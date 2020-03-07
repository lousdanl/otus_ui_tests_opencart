from attributes.attribute_common import AttributeCommon as common


def test_open_page(driver, base_url):
    driver.find_element_by_link_text(common.YOUR_STORE).click()
    assert driver.current_url[:26] == base_url
