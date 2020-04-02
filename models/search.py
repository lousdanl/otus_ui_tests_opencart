from attributes import AttributeSearch as search
from .base import Base


class Search(Base):

    def find_elements(self):
        """Find elements"""
        self._wait_element(search.INPUT_SEARCH)
        self._wait_element(search.SELECT_CATEGORIES)
        self._wait_element(search.CHECKBOX_DESCRIPTION)
        self._wait_element(search.LIST)
        self._wait_element(search.GRID)
        self._wait_element(search.SORT)
