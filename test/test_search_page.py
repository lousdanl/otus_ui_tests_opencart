from attributes.attribute_common import AttributeCommon as common
from attributes.attribute_search import AttributeSearch as search


def test_assert_elements(driver):
    driver.find_element_by_css_selector(common.INPUT_SEARCH).send_keys('macbook')
    driver.find_element_by_css_selector(common.SUBMIT_SEARCH).click()
    driver.find_element_by_css_selector(search.INPUT_SEARCH)
    driver.find_element_by_css_selector(search.SELECT_CATEGORIES)
    driver.find_element_by_css_selector(search.CHECKBOX_DESCRIPTION)
    driver.find_element_by_css_selector(search.LIST)
    driver.find_element_by_css_selector(search.GRID)
    driver.find_element_by_css_selector(search.SORT)
