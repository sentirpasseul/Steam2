from core.webdriver import WebDriver
from core.config_reader import ConfigReader
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    TIMEOUT = 10

    def __init__(self):
        self._driver = WebDriver.get_driver()
        self._poll_frequency = ConfigReader.get_poll_frequency()
        self.wait = WebDriverWait(self._driver, self.TIMEOUT, poll_frequency=self._poll_frequency)

    def wait_for_open(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))
