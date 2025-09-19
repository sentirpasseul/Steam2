from enum import StrEnum

import pytest

import tests.test_main_page
from core.webdriver import WebDriver
from core.config_reader import ConfigReader

LOCALES = ConfigReader.get_locales()


class LOCALE_COOKIE_LANGUAGE(StrEnum):
    RU = "russian"
    EN = "english"

LANGUAGE_COOKIE_NAME = ConfigReader.get_language_cookie_name()

@pytest.fixture(scope='function')
def browser(locale):
    browser = WebDriver.get_driver()
    browser.get(ConfigReader.get_link())
    browser.delete_cookie(LANGUAGE_COOKIE_NAME)
    browser.add_cookie({"name": LANGUAGE_COOKIE_NAME,
                        "value": LOCALE_COOKIE_LANGUAGE[locale.upper()].value})
    browser.refresh()

    yield browser
    WebDriver.quit_driver()


@pytest.fixture(params=LOCALES, ids=lambda v: v)
def locale(request):
    return request.param


@pytest.fixture(params=tests.test_main_page.TestMainPage.CASES, ids=lambda c: c["name"])
def case(request):
    return request.param
