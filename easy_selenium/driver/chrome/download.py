import requests
import shutil
import os
import platform
import subprocess
import re
import zipfile
from bs4 import BeautifulSoup
from termcolor import colored
from colorama import init
from ..utils import Util, BASE_PATH

init()
OSNAME = platform.system()
util = Util()
DRIVER = BASE_PATH / "executable"


class Download:
    """
    It will get the installed Chrome driver and based on the operating system
    it will download the compatible chromedriver.
    """

    if OSNAME == "Windows":
        system = "win"
    elif OSNAME == "Linux":
        system = "linux"
    else:
        system = "mac"

    def check_installed_chrome_version(self):
        try:
            if OSNAME == "Windows":
                cmd_version_output = (
                    subprocess.Popen(
                        'reg query "HKEY_CURRENT_USER\Software\Google\Chrome\BLBeacon" /v version',
                        shell=True,
                        stdout=subprocess.PIPE,
                    )
                    .stdout.read()
                    .decode("utf-8")
                )
            elif OSNAME == "Linux":
                cmd_version_output = (
                    subprocess.Popen(
                        "google-chrome --version", shell=True, stdout=subprocess.PIPE
                    )
                    .stdout.read()
                    .decode("utf-8")
                )
            elif OSNAME == "Darwin":
                cmd_version_output = (
                    subprocess.Popen(
                        "/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --version",
                        shell=True,
                        stdout=subprocess.PIPE,
                    )
                    .stdout.read()
                    .decode("utf-8")
                )
        except Exception as error:
            print(
                colored("X [Error]", "red")
                + " We couldn't find the version of the installed chrome browser."
            )
            print(f"--> {error}")
            return None
        else:
            installed_chrome_version = re.findall(
                r"([\d]+\.[\d]+\.[\d]+\.[\d]+)", cmd_version_output
            )[0].split(".")[0]
            print(
                colored("[+]", "green")
                + " You have Chrome version "
                + colored(installed_chrome_version, "blue")
                + " installed."
            )
            util.update_chrome_driver_config(version=installed_chrome_version)
            return installed_chrome_version

    def get_chrome_driver_download_link(self, version):
        base_url = "https://chromedriver.storage.googleapis.com"
        headers = {
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
        }
        response = requests.get(base_url, headers=headers)
        content = response.content.decode("utf-8")
        soup = BeautifulSoup(content, features="xml")
        keys = [key.text for key in soup.find_all("Key")]
        try:
            return [key for key in keys if self.system in key and version in key][0]
        except IndexError:
            return None

    def download_chrome_driver(self, chrome_driver_file):
        base_url = "https://chromedriver.storage.googleapis.com"
        headers = {
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
        }
        download_link = base_url + "/" + chrome_driver_file
        chrome_file_name = chrome_driver_file.split("/")[1]
        util.create_folder_if_not_exist(DRIVER)
        with requests.get(download_link, stream=True, headers=headers) as r:
            print("downloading " + colored(f"{chrome_file_name}", "blue") + " ...")
            with open(os.path.join(DRIVER, chrome_file_name), "wb") as f:
                shutil.copyfileobj(r.raw, f)

        return chrome_driver_file

    def extract_chrome_driver_zip(self, chrome_driver_file):
        global filename
        chrome_file_name = chrome_driver_file.split("/")[1]
        path = os.path.join(DRIVER, chrome_file_name)
        with zipfile.ZipFile(path, "r") as zip_ref:
            zip_ref.extractall(DRIVER)
            filename = zip_ref.namelist()[0]
        os.remove(path)
        print(colored("[+]", "green") + " Chrome driver has been installed.")
        chromedriver_path = os.path.join(DRIVER, filename)
        util.update_chrome_driver_config(chromedriver=chromedriver_path)

        return chromedriver_path
