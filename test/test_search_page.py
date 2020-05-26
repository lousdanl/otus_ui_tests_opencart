import allure

from models.user import Common, Search

SEARCH_REQUEST = "macbook"


@allure.severity(allure.severity_level.CRITICAL)
def test_assert_elements(wd, open_main_page):
    common = Common(wd)
    common.input_search_request(SEARCH_REQUEST)
    search = Search(wd)
    search.find_elements()
