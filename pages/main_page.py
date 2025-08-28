from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.search_page import SearchPage
from forms.header import HeaderForm


class MainPage(BasePage):

    FEATURED_RECOMMEND_IMG = (By.ID, "home_maincap_v7")

    def __init__(self):
        super().__init__()
        self.header = HeaderForm()


