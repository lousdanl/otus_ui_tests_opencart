from selenium.common.exceptions import NoSuchElementException

from locators import LocatorsMain as main
from models import Base


class Main(Base):

    def find_elements(self):
        """Find elements"""
        self._wait_element(main.SLIDESHOW)
        self._wait_element(main.CAROUSE)
        self._in_element(main.SWITCH_ELEMENT, main.SWITCH)
        self._wait_element(self.add_id(main.IN_CART, main.ID_MACBOOK))
        self._wait_element(self.add_id(main.IN_WISHLIST, main.ID_IPHONE))
        self._wait_element(self.add_id(main.IN_COMPARE, main.ID_CANONEOS5D))

    def select_product(self, element=main.MAC):
        """Selects product on Main Page"""
        try:
            self._click(element)
        except NoSuchElementException:
            print(f'Error: product {element} not found')
