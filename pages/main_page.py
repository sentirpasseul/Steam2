from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.search_page import SearchPage
from forms.header import HeaderForm


class MainPage(BasePage):

    FEATURED_RECOMMEND_TITLE = (By.XPATH, "//h2[@*='home_featured_and_recommended']")

    def __init__(self):
        super().__init__()
        self.search = SearchPage()
        self.header = HeaderForm()


