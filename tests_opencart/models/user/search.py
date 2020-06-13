import logging

import allure

from tests_opencart.locators import LocatorsSearch as search
from tests_opencart.models import Base


class Search(Base):
    def __init__(self, wd):
        super().__init__(wd)
        self.name = "USER_SEARCH"
        self.logger = logging.getLogger(self.name)
        self.logger.info(f"Initialization {self.name} page")

    def find_elements(self):
        """Find elements"""
        with allure.step("Поиск элементов"):
            self._wait_element(search.INPUT_SEARCH)
            self._wait_element(search.SELECT_CATEGORIES)
            self._wait_element(search.CHECKBOX_DESCRIPTION)
            self._wait_element(search.LIST)
            self._wait_element(search.GRID)
            self._wait_element(search.SORT)
