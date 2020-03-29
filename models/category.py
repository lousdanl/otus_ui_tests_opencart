from attributes import AttributeCategory as category
from .base import Base


class Category(Base):

    def find_elements(self):
        """Find elements"""
        self._wait_element(category.BREADCRUMB)
        self._wait_element(category.SHOW_LIMIT)
        self._wait_element(category.GRID)
        self._wait_element(category.LIST)
        self._wait_element(category.SORT)
