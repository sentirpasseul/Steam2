from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.search_page import SearchPage
from forms.header import HeaderForm
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    UNIQUE_MAIN_PAGE_LOC = (By.ID, "home_featured_and_recommended")

    def __init__(self):
        super().__init__()
        self.header = HeaderForm()
        self.is_open = self.wait_for_open(self.UNIQUE_MAIN_PAGE_LOC)

    def search_game(self):
        self.wait.until(EC.visibility_of_element_located(self.header.NAV_SEARCH_INPUT_LOC))
        button = self.wait.until(EC.visibility_of_element_located(self.header.NAV_SEARCH_BUTTON))
        self._driver.execute_script("arguments[0].click();", button)