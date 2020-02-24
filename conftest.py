import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome')
    parser.addoption('--url', action='store', default='http://10.0.2.15/opencart/')


@pytest.fixture(scope="session")
def wd(request):
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
    driver.maximize_window()

    yield driver
    driver.quit()
    return driver


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption('--url')
