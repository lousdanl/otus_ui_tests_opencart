from models.user import Category, Common


def test_asserts_elements(wd, open_main_page):
    common = Common(wd)
    common.menu_all_desktops()
    category = Category(wd)
    category.find_elements()
    assert category.logs_have_errors()
