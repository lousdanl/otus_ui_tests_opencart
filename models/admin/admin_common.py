import logging
import re

from locators import LocatorsAdmin as admin
from models import Base


class AdminCommon(Base):

    def __init__(self, wd):
        super().__init__(wd)
        self.name = 'ADMIN COMMON'
        self.logger = logging.getLogger(self.name)
        self.logger.info(f'Initialization {self.name} page')

    def open_catalog_products(self):
        """Go to Products page"""
        products = self._element(admin.PRODUCTS)
        products = products.get_attribute(admin.ATTRIBUTE_HREF)
        self.wd.get(products)

