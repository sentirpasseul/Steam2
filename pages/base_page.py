from core.webdriver import WebDriver
from core.config_reader import ConfigReader
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    TIMEOUT = 20
    POLL_FREQUENCY = 0.2

    def __init__(self):
        self._driver = WebDriver.get_driver()
        self.wait = WebDriverWait(self._driver, self.TIMEOUT, poll_frequency=self.POLL_FREQUENCY)
        self.ec = EC

    def wait_for_open(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))


