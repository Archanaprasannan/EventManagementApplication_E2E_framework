# from configparser import ConfigParser
#
# def read_config(section, key):
#     config = ConfigParser()
#     config.read('utils/config.ini')
#     print(config.get(section, key))
# read_config('basic info', 'url')

from configparser import ConfigParser

class ConfigReader:

    config = ConfigParser()

    config.read("configs/config_qa.ini")

    @classmethod
    def get_ui_url(cls):
        return cls.config.get("application", "ui_url")

    @classmethod
    def get_api_url(cls):
        return cls.config.get("application", "api_base_url")

    @classmethod
    def get_email(cls):
        return cls.config.get("application", "username")

    @classmethod
    def get_password(cls):
        return cls.config.get("application", "password")

    @classmethod
    def get_browser(cls):
        return cls.config.get("browser Info", "browser")

    @classmethod
    def get_headless(cls):
        return cls.config.getboolean("browser Info", "headless")

    @classmethod
    def get_screenshot(cls):
        return cls.config.get("browser Info", "screenshot")

    @classmethod
    def get_tracing(cls):
        return cls.config.get("browser Info", "tracing")