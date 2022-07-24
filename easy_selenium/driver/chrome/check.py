import os
import json


from .download import Download
from .clean import Clean
from ..utils import BASE_PATH


DRIVER = BASE_PATH / "executable"

download = Download()
clean = Clean()


def get_installed_chrome_path():
    config_file = DRIVER / "chrome.json"
    if os.path.isfile(config_file):
        chromedriver = json.load(open(config_file, "r"))["chromedriver"]
        if chromedriver:
            return chromedriver

    chrome_version = download.check_installed_chrome_version()
    if chrome_version:
        chrome_driver_name = download.get_chrome_driver_download_link(chrome_version)
        download.download_chrome_driver(chrome_driver_name)
        filename = download.extract_chrome_driver_zip(chrome_driver_name)
        path = filename
        os.chmod(path, 755)
        clean.remove_signature_in_javascript(path)
        return path


def check_user_agent(driver):
    original_user_agent_string = driver.execute_script("return navigator.userAgent")
    driver.execute_cdp_cmd(
        "Network.setUserAgentOverride",
        {
            "userAgent": original_user_agent_string.replace("Headless", ""),
        },
    )
    return driver


def check_navigator(driver):
    if driver.execute_script("return navigator.webdriver"):
        driver.execute_cdp_cmd(
            "Page.addScriptToEvaluateOnNewDocument",
            {
                "source": """

                            Object.defineProperty(window, 'navigator', {
                                value: new Proxy(navigator, {
                                has: (target, key) => (key === 'webdriver' ? false : key in target),
                                get: (target, key) =>
                                    key === 'webdriver'
                                    ? undefined
                                    : typeof target[key] === 'function'
                                    ? target[key].bind(target)
                                    : target[key]
                                })
                            });
                """
            },
        )
    return driver
