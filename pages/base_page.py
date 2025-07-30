from core.webdriver import WebDriver


class BasePage:
    TIMEOUT = 5
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
    def open(self):
        self.driver.get(self.url)
