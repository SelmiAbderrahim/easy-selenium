import time
import pickle
import random
import os
from ..logger import logger
from ..driver.utils import Util


util = Util()
BASE_PATH = os.getcwd()


class Cookies:
    """
    Save and load cookies.
    """
    def save(self, driver, url, cookies_file_name, cookies_folder_path=None):
        """
        Save cookies with .pkl extension.

        Args:
            driver (WebDriver): A chrome or Gecko driver.
            url (str): The url of the website.
            cookies_file_name (str): The name of the cookies file.
            cookies_folder_path (str): absolute path of the cookies folder
        """
        if not cookies_file_name.endswith(".pkl"):
            cookies_file_name += ".pkl"
        if cookies_folder_path:
            util.create_folder_if_not_exist(cookies_folder_path)
            path = os.path.join(cookies_folder_path, cookies_file_name)
        else:
            cookies_folder = os.path.join(BASE_PATH, "cookies")
            util.create_folder_if_not_exist(cookies_folder)
            path = os.path.join(cookies_folder, cookies_file_name)
        driver.get(url)
        time.sleep(random.randint(1, 10))
        pickle.dump(driver.get_cookies(), open(path, "wb"))
        logger.success(f"[+] {cookies_file_name} has been saved.")

    def load(self, driver, url, cookies_file_name, cookies_folder_path=None):
        """
        Load cookies from the cookies folder.

        Args:
            driver (WebDriver): A chrome or Gecko driver.
            url (str): The url of the website.
            cookies_file_name (str): The name of the cookies file.
            cookies_folder_path (str): absolute path of the cookies folder
        """
        if not cookies_file_name.endswith(".pkl"):
            cookies_file_name += ".pkl"
        if cookies_folder_path:
            util.create_folder_if_not_exist(cookies_folder_path)
            path = os.path.join(cookies_folder_path, cookies_file_name)
        else:
            cookies_folder = os.path.join(BASE_PATH, "cookies")
            util.create_folder_if_not_exist(cookies_folder)
            path = os.path.join(cookies_folder, cookies_file_name)
        driver.get(url)
        cookies = pickle.load(open(path, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)
        logger.success(f"[+] {cookies_file_name} has been loaded.")
