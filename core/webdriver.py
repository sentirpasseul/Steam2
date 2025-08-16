from selenium import webdriver
from core.config_reader import ConfigReader


class WebDriver:
    _driver = None

    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            browser = ConfigReader.get_browser_name().lower()

            try:
                cls._driver = cls._BROWSERS()[browser]()
            except KeyError:
                raise ValueError(f"Unsupported browser: {browser}")

        return cls._driver

    @classmethod
    def _BROWSERS(cls):
        return {
            "chrome": cls._create_chrome_driver,
            "firefox": cls._create_firefox_driver
        }

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
