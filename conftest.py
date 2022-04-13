import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    #выбираем браузер, дефолтный - chrome
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    #выбираем язык браузера, дефолтный - английский
    parser.addoption('--language', default='en', help='Choose browser language')


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption('language')
    #chrome
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    #firefox
    fp = webdriver.FirefoxProfile()
    fp.set_preference("intl.accept_languages", user_language)
    #choose browser
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

