from time import sleep
import pytest

from pages.main_page import MainPage
from pages.search_page import SearchPage
from enum import StrEnum



class TestMainPage:
    CASES = [
        {"name": "the_witcher", "query": "The Witcher", "price": 10},
        {"name": "fallout", "query": "Fallout", "price": 20}
    ]

    @pytest.mark.parametrize("case", CASES, ids=lambda c: c["name"])
    def test_search(self, browser, locale, case):
        main_page = MainPage()

        main_page.search_game(case["query"])

        search_page = SearchPage()

        search_page.get_prices()



