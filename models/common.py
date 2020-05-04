import logging
import re
import time
from pathlib import Path

from locators import LocatorsCommon as common
from models.base import Base


class Common(Base):

    def __init__(self, wd):
        super().__init__(wd)
        self.name = 'COMMON'
        self.logger = logging.getLogger(self.name)
        self.logger.info(f'Initialization {self.name} page')

    def token_from_url(self, pattern):
        url = self.wd.current_url
        token = re.search(pattern, url)
        return token[1]

    def add_form_input_in_body(self):
        user_token = self.token_from_url(r'user_token=(.+)&?')
        script_add_form = common.FORM_INPUT.format(user_token=user_token)
        self.wd.execute_script(script_add_form)

    def upload_file(self, filename):
        self.add_form_input_in_body()
        time.sleep(1)
        dir_file = Path(__file__).resolve().parent.parent. \
            joinpath('test_data').joinpath(filename)
        input_upload = self._element(common.INPUT_FILE)
        input_upload.send_keys(str(dir_file))

