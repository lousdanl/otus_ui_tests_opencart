import json
import os

import pytest
from selenium import webdriver

from models.admin import Admin


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome')
    parser.addoption('--url', action='store', default='http://localhost/opencart/')
    parser.addoption('--time', action='store', default=0)


@pytest.fixture()
def wd(request, base_url):
    """
    Браузер по умолчанию Chrome
    """
    browser = request.config.getoption('--browser')

    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        driver = webdriver.Chrome(options=options)
    elif browser == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        driver = webdriver.Firefox(options=options)
    else:
        raise Exception(f"{request.param} is not supported!")

    driver.implicitly_wait(request.config.getoption('--time'))
    driver.maximize_window()

    yield driver
    driver.quit()

    return driver


@pytest.fixture()
def base_url(request):
    url = request.config.getoption('--url')
    return url


@pytest.fixture()
def open_main_page(base_url, wd):
    wd.get(base_url)


@pytest.fixture()
def open_admin_page(base_url, wd):
    wd.get(base_url + 'admin')


def load_config(file):
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
    with open(config_file) as conf_file:
        target = json.load(conf_file)
    return target


@pytest.fixture()
def login(wd, open_admin_page):
    wed_config = load_config('target.json')['admin']
    username = wed_config['username']
    password = wed_config['password']
    admin = Admin(wd)
    admin.login(username, password)
    yield
    wd.find_element_by_css_selector('#header > div > ul > li:nth-child(2) > a').click()
