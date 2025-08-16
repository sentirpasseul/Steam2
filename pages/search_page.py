from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SearchPage(BasePage):

    SEARCH_INPUT = (By.XPATH, "//div[contains(@class, 'searchbar_left')]//input[@id='term']")
    SEARCH_SORT_BY = (By.XPATH, "//div[@*='sort_by_dselect_container']//button[@*='sort_by_trigger']")
    SEARCH_SORT_BY_PRICE_DESC = (By.XPATH, "//ul[@*='sort_by_droplist']//a[@*='Price_DESC']")
    SEARCH_RESULT_ITEMS = (By.XPATH, "//div[@*='search_resultsRows']")
    SEARCH_RESULT_ITEM = (By.XPATH, """
                                    (
                                        .//div[contains(@class,'discount_final_price')]
                                        |
                                        .//div[contains(@class, 'discount_final_price your_price')]/div[2]
                                    ")
                                    """
                          )
    SEARCH_RESULT_ITEM_PRICE = (By.XPATH, "//div[contains(@class, 'discount_block')]")


    def __init__(self):
        super().__init__()

    def get_price_of_item(self):
        cards = self.find_all(locator=self.SEARCH_RESULT_ITEMS)

        for card in cards:
            price_element = self.find_in(element=card, locator=self.SEARCH_RESULT_ITEM)
            price = price_element.text.strip()
            print("Цена: ", price)






