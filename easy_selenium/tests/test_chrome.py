import sys
try:
    sys.path.append("..")
    from ..driver.chrome.driver import Driver
except ImportError:
    sys.path.append(".")
    from ..driver.chrome.driver import Driver
# from ..driver.chrome.driver import Remote


def test_create_headless_driver():
    driver = Driver()
    chrome = driver.create(headless=True)
    assert chrome.title == "Home page"
    chrome.quit()


# def test_remote_chrome_driver():
#     remote = Remote()
#     chrome = remote.create()
#     assert chrome.title == "Home page"
#     chrome.quit()
