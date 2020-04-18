from models.user import Common, Search

SEARCH_REQUEST = 'macbook'


def test_assert_elements(wd, open_main_page):
    common = Common(wd)
    common.input_search_request(SEARCH_REQUEST)
    search = Search(wd)
    search.find_elements()
    assert search.logs_have_errors()
