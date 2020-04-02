from locators import LocatorsAdmin as admin
from models import Base


class AdminCommon(Base):

    def open_catalog_products(self):
        """Go to Products page"""
        products = self._element(admin.PRODUCTS)
        products = products.get_attribute(admin.ATTRIBUTE_HREF)
        self.wd.get(products)
