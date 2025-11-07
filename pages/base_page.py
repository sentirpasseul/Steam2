from core.webdriver import WebDriver
from core.config_reader import ConfigReader
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    TIMEOUT = 10

    def __init__(self):
        self._driver = WebDriver()
        self.fast_poll_frequency = ConfigReader.get_poll_frequency()
        self.wait = WebDriverWait(self._driver, self.TIMEOUT)
        self.wait_with_fast_poll_frequency = WebDriverWait(self._driver, self.TIMEOUT, poll_frequency=self.fast_poll_frequency)

