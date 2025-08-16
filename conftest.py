import pytest
from core.webdriver import WebDriver
from core.config_reader import ConfigReader

LOCALES = ConfigReader.get_locales()
LOCALE_COOKIE_LANGUAGE = {
    "ru": "russian",
    "en": "english"
}
LANGUAGE_COOKIE_NAME = ConfigReader.get_language_cookie_name()

CASES = [
    {"name": "the_witcher", "query": "The Witcher", "price": "10"},
    {"name": "fallout", "query": "Fallout", "price": "20"}
]


@pytest.fixture(scope='function')
def browser(locale):
    browser = WebDriver.get_driver()
    browser.get(ConfigReader.get_link())
    browser.delete_cookie(LANGUAGE_COOKIE_NAME)
    browser.add_cookie({"name": LANGUAGE_COOKIE_NAME,
                        "value": ConfigReader.get_cookie_value_for(locale, mapping=LOCALE_COOKIE_LANGUAGE)})
    browser.refresh()

    yield browser
    WebDriver.quit_driver()


@pytest.fixture(params=LOCALES, ids=lambda v: v)
def locale(request):
    return request.param

@pytest.fixture(params=CASES, ids=lambda c: c["name"])
def case(request):
    return request.param
