import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome')
    parser.addoption('--url', action='store', default='http://10.0.2.15/opencart/')
    parser.addoption('--time', action='store', default=0)


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption('--url')


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

    driver.get(base_url)

    yield driver
    driver.get(base_url)
    driver.quit()

    return driver
