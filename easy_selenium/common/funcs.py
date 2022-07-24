import time
from random import uniform
import sys


def send_keys_one_by_one(controller, keys, min_delay=0.05, max_delay=0.25):
    for key in keys:
        controller.send_keys(key)
        time.sleep(uniform(min_delay, max_delay))


def driver_safe_quit(driver, exit=True):
    try:
        driver.quit()
    except Exception as error:
        print(error)
        pass
    if exit:
        sys.exit()


def send_gmail(message, sender, password, receiver):
    import smtplib, ssl

    port = 587
    smtp_server = "smtp.gmail.com"
    sender_email = sender
    receiver_email = receiver
    password = password
    message = message
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


def scoll_until_the_end(driver):
    SCROLL_PAUSE_TIME = 0.5
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


def scroll_to(driver, element):
    driver.execute_script("window.scrollTo(0, arguments[0]);", element)


def get_user_agent(driver):
    return driver.execute_script("return navigator.userAgent")


def page_screenshot(driver, file_name):
    driver.get_screenshot_as_file(file_name)


def element_screenshot(element, file_name):
    element.screenshot(file_name)
