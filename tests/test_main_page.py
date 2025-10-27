from time import sleep
import pytest

from pages.main_page import MainPage
from pages.search_page import SearchPage
from enum import StrEnum

CASES = [
    {"name": "the_witcher", "query": "The Witcher", "price": 10},
    {"name": "fallout", "query": "Fallout", "price": 20}
]


class TestMainPage:

    @pytest.mark.parametrize("case", CASES, ids=['The Witcher', 'Fallout'])
    def test_search_game_prices_sorted_desc(self, browser, locale, case):
        main_page = MainPage()

        assert main_page.search_game(case["query"]), f"Игра {case["query"]} не найдена"

        search_page = SearchPage()

        assert search_page.is_prices_sort_by_desc(
            price=case['price']), f"Цены не отсортированы по убыванию"
