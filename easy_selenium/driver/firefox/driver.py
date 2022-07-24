from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import random
from fake_useragent import UserAgent
import sys

# Local Imports
from ..utils import Util
from ..constants import USER_AGENTS
from .download import Download
from easy_selenium.logger import logger
from .check import get_firefox_binary_path

sys.path.append("....")
download = Download()
util = Util()


class Driver:
    """
    Create a new driver instance (Chrome & Firefox).
    """

    def __init__(self, binary_path, user_agent=None):
        self.user_agent = user_agent
        self.generate_user_agent()
        self.binary_path = get_firefox_binary_path(binary_path)

    def generate_user_agent(self):
        try:
            ua = UserAgent()
            user_agent = ua["google chrome"]
        except IndexError:
            user_agent = random.choice(USER_AGENTS)
        self.user_agent = user_agent

    def create(self, headless=False, profile=None, mute=False):
        from ..firefox.check import get_installed_gecko_path

        path = get_installed_gecko_path()
        if not path:
            path = download.extract_gecko_driver_zip()
        if path is not None:
            options = webdriver.FirefoxOptions()
            options.headless = headless
            options.set_preference("dom.webnotifications.serviceworker.enabled", False)
            options.set_preference("dom.webnotifications.enabled", False)
            firefox_profile = webdriver.FirefoxProfile(profile)
            firefox_profile.set_preference("intl.accept_languages", "en-US")
            firefox_profile.set_preference(
                "general.useragent.override", self.user_agent
            )
            firefox_profile.set_preference("dom.webdriver.enabled", False)
            firefox_profile.set_preference("useAutomationExtension", False)
            firefox_profile.update_preferences()
            options.profile = firefox_profile
            desired = DesiredCapabilities.FIREFOX
            desired["marionette"] = True
            if mute:
                options.add_argument("--mute-audio")
                options.add_argument("--no-sandbox")
            try:
                s = Service(path)
                driver = webdriver.Firefox(
                    service=s,
                    firefox_binary=self.binary_path,
                    options=options,
                    desired_capabilities=desired,
                )
            except (TypeError, WebDriverException):
                driver = webdriver.Firefox(
                    executable_path=path,
                    firefox_binary=self.binary_path,
                    options=options,
                    desired_capabilities=desired,
                )
            except Exception as error:
                logger.critical(f"[-]  {error}")
            else:
                driver.maximize_window()
                driver.get("https://selmi.tech")
                return driver
        else:
            logger.error("Make sure you have Firefox installed on your machine!")
