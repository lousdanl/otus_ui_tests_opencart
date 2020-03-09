from attributes.attribute_admin import AttributeAdmin as admin


def test_assert_elements(wd, base_url):
    wd.get(base_url + admin.URL_ADMIN)
    wd.find_element_by_css_selector(admin.LOGIN_FORM)
    wd.find_element_by_css_selector(admin.USERNAME)
    wd.find_element_by_css_selector(admin.PASSWORD)
    wd.find_element_by_css_selector(admin.LOGIN)
    wd.find_element_by_link_text(admin.FORGOTTEN_PASSWORD)

