# from configparser import ConfigParser
#
# def read_config(section, key):
#     config = ConfigParser()
#     config.read('utils/config.ini')
#     print(config.get(section, key))
# read_config('basic info', 'url')
import os
from configparser import ConfigParser

class ConfigReader:

    config = ConfigParser()

    config = ConfigParser()

    @classmethod
    def load_config(cls, env):
        config_path = os.path.join(
            "configs",
            f"config_{env}.ini"
        )

        print(f"\nLoading config: {config_path}")

        cls.config.read(config_path)
    # @classmethod
    # def load_config(cls, env):
    #     env = os.getenv("ENV", "qa")
    #
    #     config_path = f"configs/config_{env}.ini"
    #
    #     print(f"Loading environment : {env}")
    #     print(f"Config path : {config_path}")
    #
    #     loaded_files = cls.config.read(config_path)
    #
    #     print(f"Loaded files : {loaded_files}")
    #
    #     print(cls.config.sections())

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