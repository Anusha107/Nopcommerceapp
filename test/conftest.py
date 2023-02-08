import pytest, json
from selenium.webdriver import Chrome, ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from lib.utilis.base_page_object import BasePage

URL = "https://admin-demo.nopcommerce.com/login"
#URL="https://www.amazon.in/"
SCREENSHOT_PATH = ".\\screenshots\\"


# cli tag creation
def pytest_addoption(parser):
    """
        thos deals with the implementation of the CLI commands
    """
    parser.addoption("--browser", action = "store")

# Fixture to extract the browser CLI option
@pytest.fixture
def cli_browser(request):
    return request.config.getoption("--browser")

# reading the config.json file and doing soe asserts
@pytest.fixture
def config(cli_browser):

    BROWSER = ['Chrome', 'Firefox']

    # Reading the Config.json file
    with open('config.json') as config_file:
        config = json.load(config_file)

    browser = cli_browser

    print("Browser:", browser)

    if browser is not None:
        config['browser'] = browser

    print("Config Browser:", config['browser'])

    assert config['browser'] in BROWSER
    assert isinstance(config['headless'], bool)
    
    return config

@pytest.fixture
def browser_assignment(config):
    # Pre Condition

    # Intialize the Webdriver Instance
    if config['browser'] == 'Chrome':
        opts = ChromeOptions()

        if config['headless']:
            opts.add_argument('headless')

        browser = BasePage(Chrome(executable_path=ChromeDriverManager().install(), options= opts))
        browser.visit_url(URL)

    elif config['browser'] == 'Firefox':
        pass
    else:
        raise Exception("Browser {} is not supported".format(config['browser']))

    yield browser

    # Post Condition
    browser.quit()