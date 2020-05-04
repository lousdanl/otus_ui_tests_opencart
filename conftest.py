import json
import logging
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

from context_manager import context_manager_for_read_file
from logs.listener import WdEventListener
from models.admin import AdminSession
from db.db_mysql import DbMySql


def pytest_addoption(parser):
    parser.addoption("--selenoid", action="store", default=False)
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        choices=["chrome", "firefox", "opera"],
    )
    parser.addoption("--executor", action="store", default="192.168.50.109")
    parser.addoption("--url", action="store", default="http://192.168.50.210/opencart/")
    parser.addoption("--time", action="store", default=0)
    parser.addoption("--file", action="store", default="output.log")
    parser.addoption("--alluredir allure_report", action="store")


@pytest.fixture(scope="session")
def logger(request):
    file = request.config.getoption("--file")

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    fmstr = (
        "%(asctime)s: %(name)s: %(levelname)s: %(funcName)s Line:%(lineno)d %(message)s"
    )
    datestr = "%Y-%m-%d %H:%M:%S"
    formatter = logging.Formatter(fmt=fmstr, datefmt=datestr)
    if file is None:
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)
    elif type(file) == str:
        file = Path(__file__).resolve().parent.joinpath("logs").joinpath(file)
        file_handler = logging.FileHandler(file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    else:
        raise Exception("Incorrect data")
    return logger


@pytest.fixture()
def wd(request, base_url, logger):
    """
    Браузер по умолчанию Chrome
    """
    browser = request.config.getoption("--browser")
    selenoid = request.config.getoption("--selenoid")
    executor = request.config.getoption("--executor")

    if selenoid:
        capabilities = {
            "browserName": browser,
            "version": "",
            "enableVNC": True,
            "enableVideo": False,
        }
        hub = f"http://{executor}:4444/wd/hub"
        driver = webdriver.Remote(
            command_executor=hub, desired_capabilities=capabilities
        )
    else:

        if browser == "chrome":
            options = webdriver.ChromeOptions()
            # options.add_argument('headless')
            driver = webdriver.Chrome(options=options)
        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument("-headless")
            driver = webdriver.Firefox(options=options)

    logger.info(f"Getting started browser {browser}")

    driver = EventFiringWebDriver(driver, WdEventListener(logging.getLogger("DRIVER")))
    driver.implicitly_wait(request.config.getoption("--time"))
    driver.maximize_window()

    yield driver
    driver.quit()
    logger.info(f"Browser {browser} shutdown")

    return driver


@pytest.fixture()
def base_url(request):
    url = request.config.getoption("--url")
    return url


@pytest.fixture()
def open_main_page(base_url, wd):
    wd.get(base_url)
    print("open")


@pytest.fixture()
def open_admin_page(base_url, wd):
    wd.get(base_url + "admin")


def load_config(file):
    config_file = Path(__file__).resolve().parent.joinpath(file)
    with context_manager_for_read_file(config_file) as conf_file:
        target = json.load(conf_file)
    return target


@pytest.fixture()
def login(wd, open_admin_page):
    wed_config = load_config("target.json")["admin"]
    username = wed_config["username"]
    password = wed_config["password"]
    admin = AdminSession(wd)
    admin.login(username, password)
    yield
    admin.logout()


@pytest.fixture(scope="session")
def db():
    """
    Конект к базе данных
    """
    db_config = load_config("target.json")["db"]
    dbmysql = DbMySql(
        host=db_config["host"],
        user=db_config["user"],
        password=db_config["password"],
        db=db_config["db"],
        charset=db_config["charset"],
    )
    yield dbmysql
    dbmysql.destroy()
    return dbmysql


@pytest.fixture(scope="session")
def file_new_product():
    with open(Path(__file__).resolve().parent.joinpath('test_data/new_product.json'),
              'r', encoding='utf-8') as product:
        reader = json.load(product)
    return reader
