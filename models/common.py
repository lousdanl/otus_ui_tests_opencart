import os
import re
import time

from locators import LocatorsCommon as common
from models.base import Base


class Common(Base):

    def token_from_url(self):
        url = self.wd.current_url
        pattern = r'user_token=(.+)&?'
        user_token = re.search(pattern, url)
        return user_token[1]

    def add_form_input_in_body(self):
        user_token = self.token_from_url()
        script_add_form = common.FORM_INPUT.format(user_token=user_token)
        self.wd.execute_script(script_add_form)

    @classmethod
    def get_file_direction(cls, filename):
        filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
        return filename

    def upload_file(self, filename):
        self.add_form_input_in_body()
        time.sleep(1)
        dir_file = self.get_file_direction(filename)
        input_upload = self._element(common.INPUT_FILE)
        input_upload.send_keys(dir_file)
