from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
import random
import os
from fake_useragent import UserAgent
import sys

sys.path.append("......")
# Local Imports
from .clean import Clean
from ..utils import Util
from ..constants import USER_AGENTS, SYSTEM
from .download import Download
from .check import check_user_agent, check_navigator
from easy_selenium.logger import logger

clean = Clean()
util = Util()
download = Download()


class Driver:
    """
    Create a new undetectable Chrome driver instance.
    """

    def __init__(self, user_agent=None):
        self.user_agent = user_agent
        self.generate_user_agent()

    def generate_user_agent(self):
        try:
            ua = UserAgent()
            user_agent = ua["google chrome"]
        except IndexError:
            user_agent = random.choice(USER_AGENTS)
        self.user_agent = user_agent

    def create(
        self,
        headless=False,
        profile_path="",
        mute=False,
    ):
        from .check import get_installed_chrome_path

        path = get_installed_chrome_path()

        if path is not None:
            options = webdriver.ChromeOptions()
            options.headless = headless
            options.add_argument("--start-maximized")
            options.add_argument("--lang=en-US")
            if profile_path:
                options.add_argument(r"--user-data-dir=%s" % profile_path)
            options.add_experimental_option(
                "excludeSwitches", ["enable-automation", "enable-logging"]
            )
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_argument("--log-level=3")
            options.add_experimental_option("useAutomationExtension", False)
            options.add_argument(f"user-agent={self.user_agent}")
            if mute:
                options.add_argument("--mute-audio")
                options.add_argument("--no-sandbox")
            try:
                s = Service(path)
                driver = webdriver.Chrome(service=s, options=options)
            except WebDriverException:
                driver = webdriver.Chrome(executable_path=path, options=options)
            except Exception as error:
                logger.critical(f"[-] Driver:Create {error}")
            else:
                driver = check_navigator(driver)
                driver = check_user_agent(driver)
                driver.get("https://selmi.tech")
                return driver
        else:
            logger.error("Make sure you have chrome installed on your machine!")


class Remote:
    def create(self, profile=None, debug_port=9222, control_existing_instance=False):
        options = webdriver.ChromeOptions()
        from .check import get_installed_chrome_path

        path = get_installed_chrome_path()
        if profile:
            options.add_argument(r"--user-data-dir=%s" % profile)
        if not control_existing_instance:
            self.open_new_cmd_and_run_command(
                profile_path=profile,
                port=debug_port,
            )
        options.add_experimental_option("debuggerAddress", f"127.0.0.1:{debug_port}")

        try:
            driver = webdriver.Chrome(service=Service(path), options=options)
        except TypeError:
            driver = webdriver.Chrome(executable_path=path, options=options)
        except Exception as error:
            logger.critical(f"[-] Driver:Create {error}")
        else:
            driver.get("https://selmi.tech")
            return driver

    def open_new_cmd_and_run_command(self, profile_path="", port=9222):
        """
        This function opens a new cmd window and runs the command
        a command that runs the Chrome driver in the debugging mode.
        It does not work for Firefox
        """

        if profile_path:
            cmd = f'chrome.exe --remote-debugging-port={port} --user-data-dir="{profile_path}"'
            if SYSTEM == "Windows":
                profile_path = (
                    profile_path.replace("/", "\\")
                    if "/" in profile_path
                    else profile_path
                )
        else:
            cmd = f"chrome.exe -remote-debugging-port={port}"
        if SYSTEM == "Windows":
            os.system("start cmd /k " + cmd)
        else:
            google = util.whereis_google_chrome()
            if not google:
                raise Exception("whereis: Google Chrome is not installed")
            if not profile_path:
                cmd = f"{google} --remote-debugging-port={port}"
            else:
                cmd = f'{google} --remote-debugging-port={port} --user-data-dir="{profile_path}"'
            os.system(f'gnome-terminal -- bash -c "{cmd}"')
