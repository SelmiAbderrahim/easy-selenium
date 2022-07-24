import os
import json


from ..utils import BASE_PATH, Util


DRIVER = BASE_PATH / "executable"
util = Util()


def get_installed_gecko_path():
    config_file = os.path.join(DRIVER, "gecko.json")
    if os.path.isfile(config_file):
        geckodriver = json.load(open(config_file, "r"))["geckodriver"]
        if geckodriver:
            return geckodriver

    return None


def get_firefox_binary_path(new_path=None):
    config_file = util.create_gecko_driver_config()
    if os.path.isfile(config_file):
        config = json.load(open(config_file, "r"))
        binary = json.load(open(config_file, "r"))["binary"]
        if binary:
            return binary
        elif new_path:
            path = new_path.replace("\\", "/")
            with open(DRIVER / "gecko.json", "w") as cfg:
                config["binary"] = path
                cfg.write(json.dumps(config))
                return path
    return None
