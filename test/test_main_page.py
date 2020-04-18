import allure

from models.user import Main


@allure.severity(allure.severity_level.NORMAL)
def test_assert_elements(wd, open_main_page):
    main = Main(wd)
    main.find_elements()
    assert main.logs_have_errors()
