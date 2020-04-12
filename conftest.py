import json
import logging
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

from context_manager import context_manager_for_read_file
from logs.listener import WdEventListener
from models.admin import AdminSession


def pytest_addoption(parser):
    parser.addoption('--grid', action='store', default='off', choices=['on', 'off'])
    parser.addoption('--browser', action='store', default='chrome')
    parser.addoption('--platform', action='store', default='windows')
    parser.addoption('--executor', action='store', default='localhost')
    parser.addoption('--url', action='store', default='http://192.168.50.210/opencart/')
    parser.addoption('--time', action='store', default=0)
    parser.addoption('--file', action='store', default='output.log')


@pytest.fixture(scope='session')
def logger(request):
    file = request.config.getoption('--file')

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    fmstr = "%(asctime)s: %(name)s: %(levelname)s: %(funcName)s Line:%(lineno)d %(message)s"
    datestr = "%Y-%m-%d %H:%M:%S"
    formatter = logging.Formatter(fmt=fmstr, datefmt=datestr)
    if file is None:
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)
    elif type(file) == str:
        file = Path(__file__).resolve().parent.joinpath('logs').joinpath(file)
        file_handler = logging.FileHandler(file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    else:
        raise Exception('Incorrect data')
    return logger


@pytest.fixture()
def wd(request, base_url, logger):
    """
    Браузер по умолчанию Chrome
    """
    browser = request.config.getoption('--browser')
    platform = request.config.getoption('--platform')
    grid = request.config.getoption('--grid')
    executor = request.config.getoption("--executor")

    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
    elif browser == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
    else:
        logger.exception(f"{request.param} is not supported!")
        raise Exception

    if grid == 'on':
        capabilities = options.to_capabilities()
        capabilities['platformName'] = platform
        hub = f"http://{executor}:4444/wd/hub"
        driver = webdriver.Remote(command_executor=hub, desired_capabilities=capabilities)
    elif grid == 'off':

        if browser == 'chrome':
            driver = webdriver.Chrome(options=options)
        elif browser == 'firefox':
            driver = webdriver.Firefox(options=options)

    logger.info(f'Getting started browser {browser}')
    driver = EventFiringWebDriver(driver, WdEventListener(logging.getLogger('DRIVER')))
    driver.implicitly_wait(request.config.getoption('--time'))
    driver.maximize_window()

    yield driver
    driver.quit()
    logger.info(f'Browser {browser} shutdown')

    return driver


@pytest.fixture()
def base_url(request):
    url = request.config.getoption('--url')
    return url


@pytest.fixture()
def open_main_page(base_url, wd):
    wd.get(base_url)
    print('open')


@pytest.fixture()
def open_admin_page(base_url, wd):
    wd.get(base_url + 'admin')


def load_config(file):
    config_file = Path(__file__).resolve().parent.joinpath(file)
    with context_manager_for_read_file(config_file) as conf_file:
        target = json.load(conf_file)
    return target


@pytest.fixture()
def login(wd, open_admin_page):
    wed_config = load_config('target.json')['admin']
    username = wed_config['username']
    password = wed_config['password']
    admin = AdminSession(wd)
    admin.login(username, password)
    yield
    admin.logout()
