from locators import LocatorsUserCommon as common
from models import Base


class Common(Base):

    def input_search_request(self, search_request):
        self._input(common.INPUT_SEARCH, search_request)
        self._click(common.SUBMIT_SEARCH)

    def menu_all_desktops(self):
        self._click(common.MENU_DESKTOPS)
        self._click(common.SELECT_ALL_DESKTOPS)
