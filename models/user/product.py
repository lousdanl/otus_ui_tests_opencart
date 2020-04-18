import logging

from selenium.common.exceptions import NoSuchElementException, TimeoutException

from locators import LocatorsProduct as product
from models import Base


class Product(Base):

    def __init__(self, wd):
        super().__init__(wd)
        self.name = 'USER_PRODUCT'
        self.logger = logging.getLogger(self.name)
        self.logger.info(f'Initialization {self.name} page')

    def find_elements(self):
        """Find elements"""
        self._wait_element(product.CONTENT)
        self._wait_element(product.QUANTITY)
        self._wait_element(product.IN_CART)
        self._wait_element(product.TAG_DESCRIPTION)
        self._wait_element(product.TAG_REVIEWS)

    def open_image(self):
        """Open image
        Return image element and number of images
        """
        images = self._elements(product.IMAGE_ADDITIONAL)
        image = images[0]
        self._click(image)
        image = self._wait_element(product.IMAGE_OPEN)
        number = len(images)
        return image, number

    def switch_image(self, number):
        """Click next image"""
        for i in range(number):
            self._click(product.NEXT_IMAGE)
            self._wait_element(product.IMAGE_OPEN)

    def close_image(self):
        """Close image"""
        self._click(product.IMAGE_CLOSE)

    def wait_staleness(self, image):
        """Waiting for an item to disappear"""
        self.wait_staleness_of(image)

    def select_option(self):
        """If product have option, make a selection"""
        try:
            self.menu_select_by_index(product.OPTION226, 1)
        except NoSuchElementException:
            print("Product don't have option")

    def add_to_cart(self):
        """ CLick button add product to cart"""
        try:
            button = self._wait_clickable(product.IN_CART)
            self._click(button)
        except TimeoutException:
            print(f'Error: locator {product.IN_CART} not found')

    def get_price(self):
        """ Return product's price"""
        price = self._in_element(product.CONTENT, product.PRICE)
        return price

    def get_products_name(self):
        """ Return product's name"""
        name = self._in_element(product.CONTENT, product.NAME_PRODUCT)
        name = name.text
        return name

    def alert_success(self):
        """
        Find alert success
        Return text
        """
        alert_text = self._wait_element(product.ALERT_SUCCESS)
        alert_text = alert_text.text
        return alert_text[:-2]
