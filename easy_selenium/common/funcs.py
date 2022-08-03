import time
from random import uniform
import sys
from pathlib import Path
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.webdriver import WebDriver


def send_keys_one_by_one(
        controller: WebElement,
        keys: str,
        min_delay: float = 0.05,
        max_delay: float = 0.25):
    """
    Write inputs character by character

    Args:
        - controller (WebElement): The input web element
        - keys (str): The string you'll type in the input
        - min_delay (float): Minimum time to sleep between each key stroke
        - min_delay (float): Maximum time to sleep between each key stroke
    Returns:
        None
    """
    for key in keys:
        controller.send_keys(key)
        time.sleep(uniform(min_delay, max_delay))


def driver_safe_quit(driver: WebDriver, exit: bool = False):
    """
    Close the driver instance if possible.

    Args:
        - driver (WebDriver): The driver you'll quit
        - exit (bool): Exit the program after quiting the driver

    Returns:
        None
    """
    try:
        driver.quit()
    except UnboundLocalError:
        pass
    if exit:
        sys.exit()


def send_email(
        message: str,
        sender: str,
        password: str,
        receiver: str,
        **kwargs: str) -> tuple[bool, str]:
    """
    Send emails using any mail service (default=Gmail)

    Args:
        - message (str): The content of the email
        - sender (str): The email address of the sender
        - password (str): The password app of the email
        - receiver (str): The email address of the receiver

    Kwargs:
        - smtp_server (str): The SMTP server (smpp.gmail.com)
        - port (int): the port of the mail service (587)

    Returns:
        True if success otherwise False with response
    """
    import smtplib, ssl
    smtp_server = kwargs.get('smtp_server', "smtp.gmail.com")
    port = int(kwargs.get('port', 587))
    port = port
    smtp_server = smtp_server
    sender_email = sender
    receiver_email = receiver
    password = password
    message = message
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
    except Exception as error:
        return False, error
    else:
        return True, 'Email has been sent successfully.'


def scroll_until_the_end(driver: WebDriver):
    """
    Keep scrolling until the end of the page

    Args:
        - driver (WebDriver): The driver instance

    Returns:
        None
    """
    SCROLL_PAUSE_TIME = 0.5
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


def scroll_to(driver: WebDriver, element: WebElement):
    """
    Scroll to an element

    Args:
        - driver (WebDriver): The driver instance
        - element (WebElement): The element to scroll to

    Returns:
        None
    """
    driver.execute_script("window.scrollTo(0, arguments[0]);", element)


def scroll_from_to(driver: WebDriver, x: int, y: int):
    """
    Scroll from X position to Y position

    Args:
        - driver (WebDriver): The driver instance
        - x (int): It starts scrolling from here
        - y (int): It stops scrolling here

    Returns:
        None
    """
    driver.execute_script("window.scrollTo(arguments[0], arguments[1]);", x, y)


def get_user_agent(driver: WebDriver) -> str:
    """
    REturns the user agent used in the driver

    Args:
        - driver (WebDriver): The driver instance

    Returns:
        A string of the useragent
    """
    return driver.execute_script("return navigator.userAgent")


def page_screenshot(driver: WebDriver, file_name: Path):
    """
    Takes a screenshot of the visible web page

    Args:
        - driver (WebDriver): The driver instance
        - file_name (Path): The file name or path of the image

    Returns:
        None
    """
    driver.get_screenshot_as_file(file_name)


def element_screenshot(element: WebDriver, file_name: Path):
    """
    Takes a screenshot of element

    Args:
        - driver (WebDriver): The driver instance
        - file_name (Path): The file name or path of the image

    Returns:
        None
    """
    element.screenshot(file_name)
