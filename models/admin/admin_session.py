from locators import LocatorsAdmin as admin
from models import Base


class AdminSession(Base):

    def find_elements(self):
        """Find elements"""
        self._wait_element(admin.LOGIN_FORM)
        self._wait_element(admin.USERNAME)
        self._wait_element(admin.PASSWORD)
        self._wait_element(admin.LOGIN)
        self._wait_element(admin.FORGOTTEN_PASSWORD)

    def login(self, username, password):
        """Sign in to Admin"""
        self._input(admin.USERNAME, username)
        self._input(admin.PASSWORD, password)
        self._click(admin.LOGIN)

    def logout(self):
        """Exit"""
        self._wait_click(admin.LOGOUT)
