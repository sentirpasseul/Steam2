from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HeaderForm(BasePage):
    NAV_SEARCH_INPUT_LOC = (By.XPATH, "//form[@role='search']//input[@type='text']")
    NAV_SEARCH_BUTTON = (By.XPATH, '//button[@type="submit"]')
