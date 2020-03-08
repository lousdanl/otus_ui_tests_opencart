from attributes.attribute_admin import AttributeAdmin as admin


def test_assert_elements(driver, base_url):
    driver.get(base_url + admin.URL_ADMIN)
    driver.find_element_by_css_selector(admin.LOGIN_FORM)
    driver.find_element_by_css_selector(admin.USERNAME)
    driver.find_element_by_css_selector(admin.PASSWORD)
    driver.find_element_by_css_selector(admin.LOGIN)
    driver.find_element_by_link_text(admin.FORGOTTEN_PASSWORD)

