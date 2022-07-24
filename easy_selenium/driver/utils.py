import json
import os
import platform
from pathlib import Path
import subprocess

from loguru import logger

BASE_PATH = Path(__file__).resolve().absolute().parent.parent
DRIVER = BASE_PATH / "executable"


class Util:
    def create_chrome_driver_config(self):
        self.create_folder_if_not_exist(DRIVER)
        config_file = DRIVER / "chrome.json"
        if not os.path.isfile(config_file):
            with open(config_file, "w") as config:
                data = {"system": platform.system(), "version": "", "chromedriver": ""}
                config.write(json.dumps(data))
        return config_file

    def create_gecko_driver_config(self):
        self.create_folder_if_not_exist(DRIVER)
        config_file = DRIVER / "gecko.json"
        if not os.path.isfile(config_file):
            with open(config_file, "w") as config:
                data = {
                    "system": platform.system(),
                    "version": "",
                    "geckodriver": "",
                    "binary": "",
                }
                config.write(json.dumps(data))
        return config_file

    def update_chrome_driver_config(self, version="", chromedriver=""):
        config_file = self.create_chrome_driver_config()
        config_data = json.load(open(config_file, "r"))
        if version:
            config_data["version"] = version
        if chromedriver:
            config_data["chromedriver"] = chromedriver
        with open(config_file, "w") as config:
            config.write(json.dumps(config_data))

    def update_gecko_driver_config(self, version="", geckodriver="", binary=""):
        config_file = self.create_gecko_driver_config()
        config_data = json.load(open(config_file, "r"))
        if version:
            config_data["version"] = version
        if binary:
            config_data["binary"] = binary
        if geckodriver:
            config_data["geckodriver"] = geckodriver
        with open(config_file, "w") as config:
            config.write(json.dumps(config_data))

    def whereis_google_chrome(self):
        """
        Get the path of the chrome driver
        """
        try:
            chrome_path = (
                subprocess.check_output(["whereis", "google-chrome"])
                .decode("utf-8")
                .strip()
                .split()[1]
            )
        except Exception as error:
            logger.error(error)
            return False
        return chrome_path

    def create_folder_if_not_exist(self, path):
        if not os.path.isdir(path):
            os.mkdir(path)
            return True
        return True
