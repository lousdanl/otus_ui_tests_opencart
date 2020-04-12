from pathlib import Path

from selenium.webdriver.support.abstract_event_listener import AbstractEventListener


class WdEventListener(AbstractEventListener):

    def __init__(self, logger):
        self.logger = logger

    def before_navigate_to(self, url, driver):
        self.logger.info(f"Go to {url}")

    def after_navigate_to(self, url, driver):
        self.logger.info(f"Open {url}")

    def before_navigate_back(self, driver):
        self.logger.info(f"Start navigating back")

    def after_navigate_back(self, driver):
        self.logger.info(f"Navigating back is done")

    def before_find(self, by, value, driver):
        self.logger.info(f"Looking for '{value}' with '{by}'")

    def after_find(self, by, value, driver):
        self.logger.info(f"Found element '{value}' with '{by}'")

    def before_click(self, element, driver):
        self.logger.info(f"Click on {element}")

    def after_click(self, element, driver):
        self.logger.info(f"Click on {element} is success")

    def before_execute_script(self, script, driver):
        self.logger.info(f"Executing script:'{script}'")

    def after_execute_script(self, script, driver):
        self.logger.info(f"Executing script '{script}' is done")

    def after_quit(self, driver):
        self.logger.info(f"Browser shutdown")

    def on_exception(self, exception, driver):
        self.logger.error(f"An error has occurred: {exception}")
        file = Path(__file__).resolve().parent.joinpath('screenshots').joinpath('error_screenshot.png')
        driver.save_screenshot(str(file))
