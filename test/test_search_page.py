from models import Common, Search


def test_assert_elements(wd, open_main_page):
    common = Common(wd)
    search = Search(wd)
    common.start_search()
    search.find_elements()
