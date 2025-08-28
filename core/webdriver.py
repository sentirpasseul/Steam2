from selenium import webdriver
from core.config_reader import ConfigReader
from enum import Enum


class WebDriver:
    _driver = None

    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            browser = ConfigReader.Browsers(ConfigReader.get_browser_name())
            print(browser)
            match browser:
                case ConfigReader.Browsers.CHROME:
                    cls._driver = cls._create_chrome_driver()
                case ConfigReader.Browsers.FIREFOX:
                    cls._driver = cls._create_firefox_driver()

        return cls._driver

    @classmethod
    def _create_chrome_driver(cls):
        options = webdriver.ChromeOptions()
        if ConfigReader.get_headless():
            options.add_argument("--headless=new")
        options.add_argument(f"--window-size={ConfigReader.get_window_size()}")
        return webdriver.Chrome(options=options)

    @classmethod
    def _create_firefox_driver(cls):
        options = webdriver.FirefoxOptions()
        if ConfigReader.get_headless():
            options.add_argument("--headless=new")
        driver = webdriver.Firefox(options=options)
        width, height = map(int, ConfigReader.get_window_size().split(","))
        driver.set_window_size(width, height)
        return driver

    @classmethod
    def quit_driver(cls):
        if cls._driver:
            cls._driver.quit()
            cls._driver = None
