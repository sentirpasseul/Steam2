from core.webdriver import WebDriver
from core.config_reader import ConfigReader
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    TIMEOUT = 5

    def __init__(self):
        self._driver = WebDriver.get_driver()

    def open(self, link=None):
        if link is None:
            link = getattr(self, "link", None) or ConfigReader.get_link()
        self._driver.get(link)

    def find(self, locator):
        return WebDriverWait(self._driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(locator)
        )

    def find_all(self, locator):
        return WebDriverWait(self._driver, self.TIMEOUT).until(
            EC.visibility_of_all_elements_located(locator)
        )

    def find_in(self, element, locator):
        return element.find_element(*locator)

    def find_all_in(self, element, locator):
        return element.find_elements(*locator)

    def is_element_with_text_visible(self, text, locator):
        element = self.find(locator)
        if element.text.strip().lower() == text.strip().lower():
            return element.is_displayed()
        return False

    def input_text(self, text, locator):
        return self.find(locator).send_keys(text)

    def click(self, locator):
        return self.find(locator).click()

    def select_element_by_locator(self, locator):
        return self.click(locator)

    def get_value_of_attribute(self, locator, attribute):
        element = self.find(locator)
        return element.get_attribute(attribute)