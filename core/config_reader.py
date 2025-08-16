import json
import os

class ConfigReader:
    PATH_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "browser_config.json"))
    _config_data = None
    BASE_URL = "/"

    @classmethod
    def _get_config(cls):
        if cls._config_data is None:
            with open(cls.PATH_FILE) as file:
                cls._config_data = json.load(file)
        return cls._config_data

    @classmethod
    def get_browser_name(cls):
        return cls._get_config().get("browser", "chrome")

    @classmethod
    def get_window_size(cls):
        width = cls._get_config().get("window_width", "1920")
        height = cls._get_config().get("window_height", "1080")
        return f"{width},{height}"

    @classmethod
    def get_headless(cls):
        return cls._get_config().get("headless", False)

    @classmethod
    def get_link(cls):
        return cls._get_config().get("start_url", "https://store.steampowered.com/")

    @classmethod
    def get_locales(cls):
        return cls._get_config().get("locales")

    @classmethod
    def get_language_cookie_name(cls):
        return cls._get_config().get("cookie_language_name")

    @classmethod
    def get_cookie_value_for(cls, locale: str, mapping: dict | None) -> str:
        mapping = mapping or {}
        return mapping.get(locale, locale)


