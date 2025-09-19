from time import sleep
import pytest

from pages.main_page import MainPage
from pages.search_page import SearchPage


class TestMainPage:
    CASES = [
        {"name": "the_witcher", "query": "The Witcher", "price": 10},
        {"name": "fallout", "query": "Fallout", "price": 20}
    ]

    @pytest.fixture(params=CASES, ids=lambda c: c["name"])
    def test_search(self, browser, locale, case):
        main_page = MainPage()
        search_page = SearchPage()

        main_page.is_open()
        main_page.search_game()

        search_page.is_open()
        search_page.sort_by()
        search_page.wait_loader()
        search_page.get_prices()





        print(search_page.get_prices())



