from time import sleep

from pages.main_page import MainPage
from pages.search_page import SearchPage

CASES = [
    {"name": "the_witcher", "query": "The Witcher", "price": "10"},
    {"name": "fallout", "query": "Fallout", "price": "20"}
]
def test_open_main_page(browser, locale, case):
    main_page = MainPage()
    search_page = SearchPage()

    main_page.find(main_page.FEATURED_RECOMMEND_IMG)
    main_page.input_text(locator=main_page.header.NAV_SEARCH_INPUT, text=case["query"])
    main_page.click(main_page.header.NAV_SEARCH_BUTTON)

    main_page.click(search_page.SEARCH_SORT_BY)
    main_page.click(search_page.SEARCH_SORT_BY_PRICE_DESC)
    main_page.find(search_page.SEARCH_RESULTS)
    main_page.find_element_in_dom(search_page.SEARCH_SORT_BY_PRICE_DESC_ACTIVE)

    print(search_page.get_prices())



