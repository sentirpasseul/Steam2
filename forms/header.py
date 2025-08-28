from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HeaderForm(BasePage):
    NAV_SEARCH_INPUT = (By.XPATH, "//input[@*='store_nav_search_term']")
    NAV_SEARCH_BUTTON = (By.XPATH, "//a[@*='store_search_link']//img")
