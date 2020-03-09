from attributes.attribute_common import AttributeCommon as common
from attributes.attribute_search import AttributeSearch as search


def test_assert_elements(wd):
    wd.find_element_by_css_selector(common.INPUT_SEARCH).send_keys('macbook')
    wd.find_element_by_css_selector(common.SUBMIT_SEARCH).click()
    wd.find_element_by_css_selector(search.INPUT_SEARCH)
    wd.find_element_by_css_selector(search.SELECT_CATEGORIES)
    wd.find_element_by_css_selector(search.CHECKBOX_DESCRIPTION)
    wd.find_element_by_css_selector(search.LIST)
    wd.find_element_by_css_selector(search.GRID)
    wd.find_element_by_css_selector(search.SORT)
