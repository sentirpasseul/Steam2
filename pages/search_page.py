from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SearchPage(BasePage):
    UNIQUE_SEARCH_PAGE_LOC = (By.ID, "sort_by_trigger")

    SEARCH_SORT_BY = (By.ID, "sort_by_trigger")
    SEARCH_SORT_BY_PRICE_DESC = (By.XPATH, "//a[@*='Price_DESC']")
    SEARCH_RESULTS = (By.ID, "search_results")
    SEARCH_RESULT_ITEM_FINAL_PRICE = (By.XPATH, "//div[contains(@class,'discount_final_price')]")
    LOADER_SEARCH_LOC = (By.ID, "search_result_container")

    def __init__(self):
        super().__init__()
        self.is_open = self.wait_for_open(self.UNIQUE_SEARCH_PAGE_LOC)

    def sort_by(self):
        self.wait.until(self.ec.element_to_be_clickable(self.SEARCH_SORT_BY)).click()
        self.wait.until(self.ec.element_to_be_clickable(self.SEARCH_SORT_BY_PRICE_DESC)).click()

    def wait_loader(self):
        self.wait.until(self.ec.visibility_of_element_located(self.LOADER_SEARCH_LOC))

    def get_prices(self):
        prices = self.wait.until(self.ec.visibility_of_all_elements_located(self.SEARCH_RESULT_ITEM_FINAL_PRICE))
        print(prices)
