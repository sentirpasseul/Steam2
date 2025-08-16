from time import sleep

from pages.main_page import MainPage
import pytest
from faker import Faker


@pytest.mark.pages
def test_open_main_page(browser, locale, case):
    page = MainPage()
    page.open()

    page.find(page.FEATURED_RECOMMEND_TITLE)
    page.input_text(locator=page.header.NAV_SEARCH_INPUT, text=case["query"])
    page.click(page.header.NAV_SEARCH_BUTTON)

    page.click(page.search.SEARCH_SORT_BY)
    page.click(page.search.SEARCH_SORT_BY_PRICE_DESC)

    page.is_element_with_text_visible(text=case["query"], locator=page.search.SEARCH_RESULT_ITEMS)
    page.search.get_price_of_item()



