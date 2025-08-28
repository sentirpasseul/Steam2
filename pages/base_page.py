from core.webdriver import WebDriver
from core.config_reader import ConfigReader
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    TIMEOUT = 15

    def __init__(self):
        self._driver = WebDriver.get_driver()

    def find(self, locator):
        return WebDriverWait(self._driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(locator)
        )

    def find_element_in_dom(self, locator):
        return WebDriverWait(self._driver, self.TIMEOUT).until(
            EC.presence_of_element_located(locator)
        )

    def find_text(self, locator, text):
        return WebDriverWait(self._driver, self.TIMEOUT).until(
            EC.text_to_be_present_in_element(locator, text_=text)
        )

    def find_all(self, locator):
        return WebDriverWait(self._driver, self.TIMEOUT).until(
            EC.visibility_of_all_elements_located(locator)
        )

    def is_element_with_text_visible(self, text, locator):
        element = self.find_text(locator, text)
        return element
        #if element.text.strip().lower() == text.strip().lower():
         #   return element.is_displayed()
        #return False

    def input_text(self, text, locator):
        return self.find(locator).send_keys(text)

    def click(self, locator):
        return self.find(locator).click()

    def select_element_by_locator(self, locator):
        return self.click(locator)

    def get_value_of_attribute(self, locator, attribute):
        element = self.find(locator)
        return element.get_attribute(attribute)

    def click_element(self, locator):
        return WebDriverWait(self._driver, self.TIMEOUT).until(
            EC.element_to_be_clickable(locator)
        )