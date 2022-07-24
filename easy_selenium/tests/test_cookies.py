import sys
from pathlib import Path
import os
try:
    sys.path.append("..")
    from ..driver.chrome.driver import Driver
    from ..cookies.cookies import Cookies
except ImportError:
    sys.path.append(".")
    from ..driver.chrome.driver import Driver
    from ..cookies.cookies import Cookies


def test_cookies():
    driver = Driver()
    cookie = Cookies()
    chrome = driver.create(headless=True)
    cookies_folder = Path(__file__).resolve().absolute().parent
    cookie.save(
        chrome, "https://selmi.tech", "selmi", cookies_folder_path=cookies_folder
    )
    assert os.path.isfile(cookies_folder / "selmi.pkl")
    os.remove(cookies_folder / "selmi.pkl")
    chrome.quit()
