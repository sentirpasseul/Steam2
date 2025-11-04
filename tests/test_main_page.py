from time import sleep
import pytest

from pages.main_page import MainPage
from pages.search_page import SearchPage
from enum import StrEnum


class TestMainPage:

    @pytest.mark.parametrize("name, price", [
        ("The Witcher", 10),
        ("Fallout", 20)
    ])
    def test_search_game_prices_sorted_desc(self, browser, locale, name, price):
        main_page = MainPage()
        assert main_page.wait_for_open(main_page.UNIQUE_MAIN_PAGE_LOC), "Ошибка в открытии главной страницы\n"
        main_page.search_game(name)

        search_page = SearchPage()
        assert search_page.wait_for_open(search_page.UNIQUE_SEARCH_PAGE_LOC), "Ошибка в открытии страницы поиска\n"

        prices = search_page.get_prices(price=price)
        assert prices == sorted(prices, reverse=True), (f"Цены {prices} не отсортированы по умолчанию "
                                                        f"у игры {name}\n на {locale}")
