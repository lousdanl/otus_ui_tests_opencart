from attributes.attribute_admin import AttributeAdmin as admin


# For this test, you need to add your URL to the command line
def test_assert_elements(driver):
    driver.find_element_by_css_selector(admin.LOGIN_FORM)
    driver.find_element_by_css_selector(admin.USERNAME)
    driver.find_element_by_css_selector(admin.PASSWORD)
    driver.find_element_by_css_selector(admin.LOGIN)
    driver.find_element_by_link_text(admin.FORGOTTEN_PASSWORD)
