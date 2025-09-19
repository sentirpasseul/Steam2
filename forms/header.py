from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HeaderForm(BasePage):
    NAV_SEARCH_INPUT_LOC = (By.ID, "store_nav_search_term")
    NAV_SEARCH_BUTTON = (By.ID, "store_search_link")
