import requests
import platform
import io
import zipfile
from bs4 import BeautifulSoup
from termcolor import colored
from colorama import init


from ..utils import Util, BASE_PATH

OSNAME = platform.system()
init()
util = Util()
DRIVER = BASE_PATH / "executable"


class Download:
    """
    It will get the installed Chrome driver and based on the operating system
    it will download the compatible chromedriver.
    """

    def get_gecko_driver_latest_link(self):
        base_url = "https://github.com/mozilla/geckodriver/releases/latest"
        headers = {
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
        }
        response = requests.get(base_url, headers=headers)
        content = response.content.decode("utf-8")
        soup = BeautifulSoup(content, features="lxml")
        urls = [
            link.get("href")
            for link in soup.find_all("a")
            if "geckodriver-v" in link.get("href")
        ]
        try:
            if OSNAME == "Windows":
                return (
                    "https://github.com"
                    + [url for url in urls if "win32.zip" in url][0]
                )
            elif OSNAME == "Linux":
                return (
                    "https://github.com"
                    + [url for url in urls if "linux32.tar.gz" in url][0]
                )
            else:
                return (
                    "https://github.com"
                    + [url for url in urls if "macos.tar.gz" in url][0]
                )
        except IndexError:
            return None

    def download_gecko_driver(self):
        url = self.get_gecko_driver_latest_link()
        headers = {
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
        }
        try:
            response = requests.get(url, stream=True, headers=headers)
            return response
        except Exception as error:
            print(colored("Geckodriver:Download - ", "red") + str(error))
            return None

    def extract_gecko_driver_zip(self):
        response = self.download_gecko_driver()
        if response:
            z = zipfile.ZipFile(io.BytesIO(response.content))
            z.extractall(DRIVER)
            print(colored("[+]", "green") + " Gecko driver has been installed.")
            geckodriver_path = DRIVER / "geckodriver"
            geckodriver_path = (
                str(geckodriver_path) + ".exe" if OSNAME == "Windows" else ""
            )
            util.update_gecko_driver_config(geckodriver=geckodriver_path)
            return geckodriver_path
        return None
