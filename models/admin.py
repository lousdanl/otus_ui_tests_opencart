import time

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

from attributes import AttributeAdmin as admin
from models import generate_data
from .base import Base


class Admin(Base):

    def get_count_pages(self):
        """Return count pages with products"""
        count_pages = self._element(admin.COUNT_PAGES).text
        count_pages = count_pages[-8]
        return int(count_pages)

    def click_next_page(self):
        pagination = self._in_element(admin.ELEMENT_PAGINATION, admin.NEXT_PAGE)
        self._click(pagination)

    def get_products_from_one_page(self):
        """Return quantity  products on one page"""
        products = self._elements(admin.COUNT_PRODUCTS)
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
                get_name = self._in_elements(product, admin.TABLE_PROD_NAME)[0]
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
        self._wait_click(admin.ADD_PRODUCT)

    def click_save_changes(self):
        self._click(admin.BUTTON_SAVE)

    def click_edit_product(self, product):
        button = self._in_element(product, admin.BUTTON_EDIT)
        self._click(button)

    def click_button_copy(self):
        self._click(admin.BUTTON_COPY)

    def click_button_delete(self):
        self._click(admin.BUTTON_DELETE)

    def product_data(self):
        """Gets names of all products generates a new one, no matches"""
        products = self.get_name_all_products()
        while True:
            product_id = generate_data.random_data(3)
            product_name = 'Product ' + product_id
            if product_name not in products:
                return product_name

    def product_price(self, one_product):
        """Looking for price product"""
        product = self._in_elements(one_product, admin.TAMLE_PROD_PRICE)[0]
        try:
            price_before = self._in_element(product, admin.PRICE_BEFORE).text
            price = price_before
        except StaleElementReferenceException:
            price = product.text
        except NoSuchElementException:
            price = product.text
        price = price.replace('$', '').split('.')
        return int(price[0])

    def select_product(self, product):
        """Clicks on checkbox to focus to product"""
        product_name = self._in_elements(product, admin.TABLE_PROD_NAME)[0]
        product_name = product_name.text
        checkbox = self._in_element(product, admin.CHECKBOX_PROD)
        self._click(checkbox)
        return product_name

    def section_general(self):
        self._wait_click(admin.TAB_GENERAL)

    def section_data(self):
        self._wait_click(admin.TAB_DATA)

    def section_special(self):
        self._wait_click(admin.TAB_SPECIAL)

    def assert_validation_add_form(self):
        """Verify that the empty field is not saved, all important fields must be filled"""
        self.click_save_changes()
        alert_warning = self._wait_element(admin.ALERT_WARNING)
        alert_warning = alert_warning.text
        alert_warning = alert_warning[: -2].strip()
        assert admin.TEXT_WARNING_ALERT == alert_warning
        assert 3 == len(self._elements(admin.DANGER_TEXT))

    def fill_general(self, product_name):
        """Fills fields, name and title"""
        self.section_general()
        self._input(admin.PRODUCT_NAME, product_name)
        self._input(admin.META_TAG_TITLE, product_name)

    def send_keys_price(self, price):
        """Fills price"""
        self._input(admin.PRICE_TAB_DATA, price)

    def fill_data(self, product_name):
        """Fills fields, model, quantity, sort, status"""
        self.section_data()
        self.send_keys_price(100)
        self._input(admin.MODEL, product_name)
        self._input(admin.QUANTITY, 10)
        self._input(admin.SORT, 20)
        self.menu_select(admin.STATUS, '1')

    def edit_price_in_section_special(self, price):
        """Fills price of sale"""
        self.section_special()
        self._input(admin.PRICE_TAB_SECTION, price)

    def edit_price(self, product_price):
        """Changes price"""
        old_price = product_price
        new_price = old_price + 1
        self.section_data()
        self.send_keys_price(new_price)
        return new_price

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
        self._wait_element(admin.ALERT_SUCCESS)
