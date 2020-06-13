import json
import logging
from pathlib import Path

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

from logs.listener import WdEventListener
from models.admin import AdminSession
from db.db_mysql import DbMySql
from ssh.ssh_client import SshClient


def pytest_addoption(parser):
    parser.addoption("--selenoid", action="store", default=False)
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        choices=["chrome", "firefox"]
    )
    parser.addoption("--executor", action="store", default="192.168.50.45")
    # "http://192.168.50.210/opencart/" # xampp
    parser.addoption("--url", action="store", default="http://192.168.50.45/")  # bitnami docker

    parser.addoption("--time", action="store", default=0)
    parser.addoption("--file", action="store", default="output.log")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.outcome != 'passed':
        item.status = 'failed'
    else:
        item.status = 'passed'


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
        file = Path.cwd().resolve().joinpath("logs").joinpath(file)
        file_handler = logging.FileHandler(str(file), encoding='utf-8')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    else:
        raise Exception("Incorrect data")
    return logger


def data_on_failed_test(browser, driver, request):
    if browser == 'chrome':
        if request.node.status == 'failed':
            browser_logs = driver.get_log("browser")
            allure.attach(body=str(browser_logs), name="Browser logs", attachment_type=AttachmentType.TEXT)
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


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
            "acceptSslCerts": True
        }
        hub = f"http://{executor}:4444/wd/hub"
        driver = webdriver.Remote(
            command_executor=hub, desired_capabilities=capabilities
        )
    else:

        if browser == "chrome":
            options = webdriver.ChromeOptions()
            # options.add_argument('headless')
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--ignore-ssl-errors')
            driver = webdriver.Chrome(options=options)
        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--ignore-ssl-errors')
            options.add_argument("-headless")
            driver = webdriver.Firefox(options=options)

    logger.info(f"Getting started browser {browser}")

    driver = EventFiringWebDriver(driver, WdEventListener(logging.getLogger("DRIVER")))
    driver.implicitly_wait(request.config.getoption("--time"))
    driver.maximize_window()

    yield driver
    data_on_failed_test(browser, driver, request)
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


@pytest.fixture()
def open_admin_page(base_url, wd):
    wd.get(base_url + "admin")


def load_config(file):
    config_file = Path.cwd().resolve().joinpath(file)
    with open(str(config_file), 'r') as conf_file:
        target = json.load(conf_file)
    return target


@pytest.fixture()
def login(wd, open_admin_page):
    wed_config = load_config("credentials.json")["admin"]
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
    db_config = load_config("credentials.json")["db"]
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
    with open(
        str(Path.cwd().joinpath("test_data/new_product.json")),
        "r",
        encoding="utf-8",
    ) as product:
        reader = json.load(product)
    return reader


@pytest.fixture()
def ssh():
    ssh_config = load_config("credentials.json")["ssh"]
    client = SshClient(
        hostname=ssh_config["hostname"],
        username=ssh_config["username"],
        password=ssh_config["password"],
        port=ssh_config["port"]
    )
    yield client
    client.destroy()
    return client
