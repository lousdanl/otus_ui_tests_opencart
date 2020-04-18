import allure


@allure.severity(allure.severity_level.CRITICAL)
def test_open_page(wd, open_main_page, base_url):
    assert wd.current_url == base_url
