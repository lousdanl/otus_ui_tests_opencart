import logging

from locators import LocatorsAdmin as admin
from models import Base


class AdminSession(Base):
    def __init__(self, wd):
        super().__init__(wd)
        self.name = "ADMIN_SESSION"
        self.logger = logging.getLogger(self.name)
        self.logger.info(f"Initialization {self.name} page")

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
        self._wait_click(admin.LOGIN)

    def logout(self):
        """Exit"""
        self._wait_click(admin.LOGOUT)
