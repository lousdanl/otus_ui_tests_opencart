import logging

import allure

from locators import LocatorsCategory as category
from models.base import Base


class Category(Base):
    def __init__(self, wd):
        super().__init__(wd)
        self.name = "USER_CATEGORY"
        self.logger = logging.getLogger(self.name)
        self.logger.info(f"Initialization {self.name} page")

    def find_elements(self):
        """Find elements"""
        with allure.step("Поиск элементов"):
            self._wait_element(category.BREADCRUMB)
            self._wait_element(category.SHOW_LIMIT)
            self._wait_element(category.GRID)
            self._wait_element(category.LIST)
            self._wait_element(category.SORT)
