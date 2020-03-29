from .base import Base
from attributes import AttributeAdmin as admin


class AdminCommon(Base):

    def open_catalog_products(self):
        """Go to Products page"""
        products = self._element(admin.PRODUCTS)
        products = products.get_attribute(admin.ATTRIBUTE_HREF)
        self.wd.get(products)
