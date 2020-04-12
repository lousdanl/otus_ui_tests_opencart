from models.user import Main


def test_assert_elements(wd, open_main_page):
    main = Main(wd)
    main.find_elements()
    assert main.get_logs_browser()
