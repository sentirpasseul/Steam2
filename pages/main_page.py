from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.search_page import SearchPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



class MainPage(BasePage):
    UNIQUE_MAIN_PAGE_LOC = (By.XPATH, "//div[contains(@class, 'home_page_body')]")
    NAV_SEARCH_INPUT_LOC = (By.XPATH, "//form[@role='search']//input[@type='text']")
    NAV_SEARCH_BUTTON = (By.XPATH, '//button[@type="submit"]')

    def wait_for_open(self):
        try:
            self.wait.until(EC.presence_of_element_located(self.UNIQUE_MAIN_PAGE_LOC))
            return True
        except TimeoutException:
            return False

    def search_game(self, name):
        self.wait.until(EC.visibility_of_element_located(self.NAV_SEARCH_INPUT_LOC)).send_keys(name)
        self.wait.until(EC.visibility_of_element_located(self.NAV_SEARCH_BUTTON)).click()
