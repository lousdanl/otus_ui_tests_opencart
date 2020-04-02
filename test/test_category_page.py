from models import Category, Common


def test_asserts_elements(wd, open_main_page):
    common = Common(wd)
    category = Category(wd)
    common.menu_all_desktops()
    category.find_elements()

