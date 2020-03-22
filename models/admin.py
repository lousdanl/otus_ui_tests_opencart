import time

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from attributes.attribute_admin import AttributeAdmin as admin
from models import generate_data


class Admin:
    def __init__(self, wd):
        self.wd = wd

    @property
    def wait(self):
        return WebDriverWait(self.wd, 10)

    def find_elements(self):
        """Find elements"""
        self.wd.find_element_by_css_selector(admin.LOGIN_FORM)
        self.wd.find_element_by_css_selector(admin.USERNAME)
        self.wd.find_element_by_css_selector(admin.PASSWORD)
        self.wd.find_element_by_css_selector(admin.LOGIN)
        self.wd.find_element_by_link_text(admin.FORGOTTEN_PASSWORD)

    def login(self, username, password):
        """Sign in to Admin"""
        self.wd.find_element_by_css_selector(admin.USERNAME).send_keys(username)
        self.wd.find_element_by_css_selector(admin.PASSWORD).send_keys(password)
        self.wd.find_element_by_css_selector(admin.LOGIN).click()

    def open_catalog_products(self):
        """Go to Products page"""
        products = self.wd.find_element_by_css_selector(admin.PRODUCTS)
        products = products.get_attribute('href')
        self.wd.get(products)

    def get_count_pages(self):
        """Return count pages with products"""
        count_pages = self.wd.find_element_by_css_selector(admin.COUNT_PAGES).text
        count_pages = count_pages[-8]
        return int(count_pages)

    def click_next_page(self):
        pagination = self.wd.find_element_by_css_selector(admin.ELEMENT_PAGINATION)
        pagination.find_element_by_css_selector(admin.NEXT_PAGE).click()

    # def to_first_page(self):
    #     """Go to main Products page if page not first"""
    #     url = self.wd.current_url
    #     if 'page=' in url:
    #         self.wd.find_element_by_xpath("//*[contains(text(), '1')]").click()

    def get_products_from_one_page(self):
        """Return quantity  products on one page"""
        products = self.wd.find_elements_by_css_selector(admin.COUNT_PRODUCTS)
        if int(len(products)) > 0:
            return products
        else:
            raise ValueError

    def get_name_all_products(self):
        """Return name of all products from all pages"""
        count_pages = self.get_count_pages()
        list_products = []
        for i in range(count_pages):
            count_products = self.get_products_from_one_page()
            for product in count_products:
                get_name = product.find_elements_by_css_selector(admin.TABLE_PROD_NAME)[0]
                get_name = get_name.text
                list_products.append(get_name)
            if count_pages > 1:
                self.click_next_page()
                time.sleep(0.1)
            else:
                break
        return list_products

    def get_one_product(self, number):
        """Return one product"""
        product = self.get_products_from_one_page()[number]
        return product

    def click_new_product(self):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, admin.ADD_PRODUCT))).click()

    def click_save_changes(self):
        self.wd.find_element_by_css_selector(admin.BUTTON_SAVE).click()

    @classmethod
    def click_edit_product(cls, product):
        product.find_element_by_css_selector(admin.BUTTON_EDIT).click()

    def click_button_copy(self):
        self.wd.find_element_by_css_selector(admin.BUTTON_COPY).click()

    def click_button_delete(self):
        self.wd.find_element_by_css_selector(admin.BUTTON_DELETE).click()

    def product_data(self):
        """Gets names of all products generates a new one, no matches"""
        products = self.get_name_all_products()
        while True:
            product_id = generate_data.random_data(3)
            product_name = 'Product ' + product_id
            if product_name not in products:
                return product_name

    @classmethod
    def product_price(cls, one_product):
        """Looking for price product"""
        product = one_product.find_elements_by_css_selector(admin.TAMLE_PROD_PRICE)[0]
        try:
            price_before = product.find_element_by_css_selector(admin.PRICE_BEFORE).text
            price = price_before
        except StaleElementReferenceException:
            price = product.text
        except NoSuchElementException:
            price = product.text
        price = price.replace('$', '').split('.')
        return int(price[0])

    @classmethod
    def select_product(cls, product):
        """Clicks on checkbox to focus to product"""
        product_name = product.find_elements_by_css_selector(admin.TABLE_PROD_NAME)[0]
        product_name = product_name.text
        product.find_element_by_css_selector(admin.CHECKBOX_PROD).click()
        return product_name

    def section_general(self):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, admin.TAB_GENERAL))).click()

    def section_data(self):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, admin.TAB_DATA))).click()

    def section_special(self):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, admin.TAB_SPECIAL))).click()

    def assert_validation_add_form(self):
        """Verify that the empty field is not saved, all important fields must be filled"""
        self.click_save_changes()
        alert_warning = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, admin.ALERT_WARNING)))
        alert_warning = alert_warning.text
        alert_warning = alert_warning[: -2].strip()
        assert admin.TEXT_WARNING_ALERT == alert_warning
        count_warning_text = len(self.wd.find_elements_by_css_selector(admin.DANGER_TEXT))
        assert 3 == count_warning_text

    def fill_general(self, product_name):
        """Fills fields, name and title"""
        self.section_general()
        self.wd.find_element_by_css_selector(admin.PRODUCT_NAME).send_keys(product_name)
        self.wd.find_element_by_css_selector(admin.META_TAG_TITLE).send_keys(product_name)

    def send_keys_price(self, price):
        """Fills price"""
        input_price = self.wd.find_element_by_css_selector(admin.PRICE_TAB_DATA)
        input_price.clear()
        input_price.send_keys(price)

    def fill_data(self, product_name):
        """Fills fields, model, quantity, sort, status"""
        self.section_data()
        self.send_keys_price(100)
        model = self.wd.find_element_by_css_selector(admin.MODEL)
        model.clear()
        model.send_keys(product_name)
        quantity = self.wd.find_element_by_css_selector(admin.QUANTITY)
        quantity.clear()
        quantity.send_keys(10)
        sort = self.wd.find_element_by_css_selector(admin.SORT)
        sort.clear()
        sort.send_keys(20)
        status = Select(self.wd.find_element_by_css_selector(admin.STATUS))
        status.select_by_value('1')

    def edit_price_in_section_special(self, price):
        """Fills price of sale"""
        self.section_special()
        input_price = self.wd.find_element_by_css_selector(admin.PRICE_TAB_SECTION)
        input_price.clear()
        input_price.send_keys(price)

    def edit_price(self, product_price):
        """Changes price"""
        old_price = product_price
        new_price = old_price + 1
        self.section_data()
        self.send_keys_price(new_price)
        return new_price

    def select_product_by_name(self, product_name):
        """Selects product by name and Clicks on checkbox to focus to product"""
        product = self.wd.find_elements_by_xpath(f"//*[contains(text(), '{product_name}')]/..")[0]
        product.find_element_by_css_selector(admin.CHECKBOX_PROD).click()

    def count_same_products(self, product_name):
        """Counts the number of identical names in the list
        Returns count"""
        products = self.get_name_all_products()
        count_same_product = 0
        for name_in_list in products:
            if name_in_list == product_name:
                count_same_product += 1
        return count_same_product

    @classmethod
    def assert_count_same_products(cls, count):
        if count > 1:
            return True
        else:
            return False

    def accept_web_alert(self):
        alert = self.wd.switch_to.alert
        alert.accept()

    def wait_alert_success(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, admin.ALERT_SUCCESS)))
