from locators import LocatorsCategory as category
from models.base import Base


class Category(Base):

    def find_elements(self):
        """Find elements"""
        self._wait_element(category.BREADCRUMB)
        self._wait_element(category.SHOW_LIMIT)
        self._wait_element(category.GRID)
        self._wait_element(category.LIST)
        self._wait_element(category.SORT)
