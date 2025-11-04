from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import re
from selenium.webdriver.support import expected_conditions as EC


class SearchPage(BasePage):
    UNIQUE_SEARCH_PAGE_LOC = (By.ID, "sort_by_trigger")

    SEARCH_SORT_BY = (By.ID, "sort_by_trigger")
    SEARCH_SORT_BY_PRICE_DESC = (By.ID, "Price_DESC")
    SEARCH_RESULTS = (By.ID, "search_results")
    SEARCH_RESULT_ITEM_FINAL_PRICE = (By.XPATH, "//div[contains(@class,'discount_final_price')]")
    LOADER_SEARCH_LOC = (By.XPATH, "//*[@id='search_result_container' and @style='opacity: 0.5;']")

    def sort_by_price_desc(self):
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_SORT_BY)).click()
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_SORT_BY_PRICE_DESC)).click()

    def wait_loader(self):
        self.wait.until(EC.visibility_of_element_located(self.LOADER_SEARCH_LOC))
        self.wait.until_not(EC.visibility_of_element_located(self.LOADER_SEARCH_LOC))

    def get_prices(self, price=10):
        self.sort_by_price_desc()
        self.wait_loader()
        prices_elements = self.wait.until(
            EC.visibility_of_all_elements_located(self.SEARCH_RESULT_ITEM_FINAL_PRICE))
        prices = []
        for price in prices_elements[:price]:
            match = re.search(r"\d+(?:[\.,]\d+)?", price.text)
            if match:
                prices.append(float(match.group()))
            if match is None:
                prices.append(0)

        return prices
