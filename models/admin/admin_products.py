import json
import logging
import re
import time
from pathlib import Path

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

from context_manager import context_manager_for_read_file, context_manager_for_correction_file
from locators import LocatorsAdmin as admin
from models import Base, Common


class AdminProducts(Common, Base):

    def __init__(self, wd):
        super().__init__(wd)
        self.name = 'ADMIN_PRODUCTS'
        self.logger = logging.getLogger(self.name)
        self.logger.info(f'Initialization {self.name} page')

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
            raise Exception

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
        self._click(admin.FIRST_PAGE)
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
        self._wait_click(admin.BUTTON_DELETE)

    def click_button_cancel_edit(self):
        self._wait_click(admin.BUTTON_CANCEL_EDIT)

    @classmethod
    def read_product_file(cls, file):
        with context_manager_for_read_file(file) as product_id_file:
            reader = json.load(product_id_file)
            product_id = reader['product']
            return product_id

    @classmethod
    def write_product_file(cls, file, product_id):
        with context_manager_for_correction_file(file) as product_id_file:
            product = {'product': product_id}
            json.dump(product, product_id_file, indent=2)

    def product_data(self):
        """Gets names of all products generates a new one, no matches"""
        products = self.get_name_all_products()
        product_file = Path(__file__).resolve().parent.parent.parent. \
            joinpath('test_data').joinpath('product_file.json')
        product_id = self.read_product_file(product_file)
        while True:
            product_id = int(product_id)
            product_id += 1
            product_id = str(product_id)
            product_name = 'Product ' + product_id
            product_model = 'Model ' + product_id
            if product_name not in products:
                self.write_product_file(product_file, product_id)
                return product_name, product_model

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

    def section_image(self):
        self._wait_click(admin.TAB_IMAGE)

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

    def fill_data(self, product_model):
        """Fills fields, model, quantity, sort, status"""
        self.section_data()
        self.send_keys_price(100)
        self._input(admin.MODEL, product_model)
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

    def select_edit_image(self):
        self._click(admin.EDIT_IMAGE)
        self._click(admin.BUTTON_EDIT_IMAGE)
        self._wait_element(admin.BUTTON_UPLOAD)

    def select_new_image(self, image):
        new_image = self.add_id(admin.ATTRIBUTE_IMAGE, image)
        self._click(new_image)

    def close_modal_edit_image(self):
        self._wait_click(admin.BUTTON_CLOSE)

    def added_image(self, image):
        self.section_image()
        self.select_edit_image()
        self.upload_file(image)
        time.sleep(1)
        self.accept_web_alert()
        self.select_new_image(image)

    def get_product_id_from_page(self, product):
        button = self._in_element(product, admin.BUTTON_EDIT)
        attributes = self.wd.execute_script(admin.SCRIPT_FIND_ATTRIBUTES, button)
        url = attributes.get('href')
        product_id = re.search(r'product_id=(\d+)?', url).group(1)
        return int(product_id)
