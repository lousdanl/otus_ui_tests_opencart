from attributes import AttributeCommon as common
from .base import Base


class Common(Base):

    def start_search(self):
        self._input(common.INPUT_SEARCH, 'macbook')
        self._click(common.SUBMIT_SEARCH)

    def menu_all_desktops(self):
        self._click(common.MENU_DESKTOPS)
        self._click(common.SELECT_ALL_DESKTOPS)
