from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.search_page import SearchPage
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    UNIQUE_MAIN_PAGE_LOC = (By.XPATH, "//div[contains(@class, 'home_page_body')]")
    NAV_SEARCH_INPUT_LOC = (By.XPATH, "//form[@role='search']//input[@type='text']")
    NAV_SEARCH_BUTTON = (By.XPATH, '//button[@type="submit"]')

    def search_game(self, query):
        self.wait_for_open(self.UNIQUE_MAIN_PAGE_LOC)
        self.wait.until(EC.visibility_of_element_located(self.NAV_SEARCH_INPUT_LOC)).send_keys(query)
        self.wait.until(EC.visibility_of_element_located(self.NAV_SEARCH_BUTTON)).click()
