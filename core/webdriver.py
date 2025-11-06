from selenium import webdriver
from core.config_reader import ConfigReader


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
        for option in ConfigReader.get_options_for_browser():
            match option:
                case "--window-size":
                    options.add_argument(option + f"={ConfigReader.get_window_size()}")
                case "--headless":
                    if ConfigReader.get_headless():
                        options.add_argument(option)
        return webdriver.Chrome(options=options)

    @classmethod
    def _create_firefox_driver(cls):
        options = webdriver.FirefoxOptions()
        width, height = ConfigReader.get_window_size().split(",")
        driver = webdriver.Firefox(options=options)
        for option in ConfigReader.get_options_for_browser():
            match option:
                case '--window-size':
                    driver.set_window_size(width, height)
                case "--headless":
                    options.add_argument(option)
        return driver

    @classmethod
    def quit_driver(cls):
        if cls._driver:
            cls._driver.quit()
            cls._driver = None
