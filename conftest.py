from enum import StrEnum

import pytest
from core.webdriver import WebDriver
from core.config_reader import ConfigReader

LOCALES = ConfigReader.get_locales()

class LocaleCookieLanguage(StrEnum):
    RU = "russian"
    EN = "english"


LANGUAGE_COOKIE_NAME = ConfigReader.get_language_cookie_name()
COUNTRY_COOKIE_NAME = ConfigReader.get_country_cookie_name()


@pytest.fixture(scope='function')
def browser(locale):
    browser = WebDriver()
    browser.get(ConfigReader.get_link())

    browser.delete_cookie(LANGUAGE_COOKIE_NAME)
    browser.delete_cookie(COUNTRY_COOKIE_NAME)

    browser.add_cookie({"name": LANGUAGE_COOKIE_NAME,
                        "value": locale.value})
    browser.add_cookie({
        "name": COUNTRY_COOKIE_NAME,
        "value": locale.name})
    browser.refresh()

    yield browser
    WebDriver.quit_driver()


@pytest.fixture(params=[LocaleCookieLanguage.RU, LocaleCookieLanguage.EN])
def locale(request):
    return request.param
