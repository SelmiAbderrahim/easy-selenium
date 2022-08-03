import random
import os
import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from ...logger import logger
from ...driver.utils import Util
from ...cookies.cookies import Cookies
from ...common.funcs import send_keys_one_by_one


WORKING_DIRECTORY = os.getcwd()


class Login(Cookies, Util):
    """
    Automate Google authentication.

    Args:
        email (str): The Gmail address
        password (str): The Gmail password

    Returns:
        The return value. True for success, False otherwise
    """
    BASE_URL = "https://www.youtube.com"

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.cookie_name = f"google_{email}"
        self.cookie_folder = os.path.join(WORKING_DIRECTORY, "cookies")
        self.create_folder_if_not_exist(self.cookie_folder)

    def please_update_your_browser(self, driver: WebDriver):
        waitt = WebDriverWait(driver, 5)
        action = ActionChains(driver)
        try:
            return_to_youtube = waitt.until(
                EC.presence_of_element_located((
                    By.XPATH, (
                        "//a[@id= 'return-to-youtube']"
                    )
                ))
            )
        except TimeoutException:
            pass
        else:
            action.move_to_element(return_to_youtube).click().perform()

    def get_sign_in_button(self, driver: WebDriver):
        waitt = WebDriverWait(driver, 5)
        try:
            signin = waitt.until(
                EC.presence_of_element_located((
                    By.XPATH, (
                        "//div[@id= 'buttons']/ytd-button-renderer"
                        "/a[contains(@class, 'ytd-button-renderer')]"
                    )
                ))
            )
        except TimeoutException:
            return None
        else:
            return signin

    def credentials(self, driver: WebDriver) -> bool:
        waitt = WebDriverWait(driver, 5)
        action = ActionChains(driver)
        try:
            email_input = waitt.until(
                EC.presence_of_element_located((
                    By.XPATH, (
                        "//input[@type= 'email']"
                    )
                ))
            )
        except TimeoutException:
            email_input = waitt.until(
                EC.presence_of_element_located((
                    By.XPATH, (
                        "//input[@id= 'identifierId']"
                    )
                ))
            )
        try:
            next_button = waitt.until(
                EC.presence_of_element_located((
                    By.XPATH, (
                        "//button[text()='Next']"
                    )
                ))
            )
        except TimeoutException:
            next_button = waitt.until(
                EC.presence_of_all_elements_located((
                    By.TAG_NAME, "button"
                ))
            )[2]
        send_keys_one_by_one(email_input, self.email)
        action.move_to_element(next_button).click().perform()
        time.sleep(random.randint(1, 3))
        try:
            password_input = waitt.until(
                EC.presence_of_element_located((
                    By.XPATH, (
                        "//input[@type= 'password']"
                    )
                ))
            )
        except TimeoutException:
            password_input = waitt.until(EC.presence_of_element_located((
                By.XPATH, (
                    "//input[@name= 'password']"
                )
            )))
        try:
            next_button2 = waitt.until(EC.presence_of_element_located(
                (By.XPATH, "//button[text()='Next']"))
            )
        except TimeoutException:
            next_button2 = waitt.until(EC.presence_of_all_elements_located((
                By.TAG_NAME, "button"
            )))[1]
        time.sleep(random.randint(1, 3))
        send_keys_one_by_one(password_input, self.password)
        action.move_to_element(next_button2).click().perform()
        time.sleep(random.randint(1, 3))
        if self.get_sign_in_button(driver):
            return True
        else:
            False

    def login_cookies(self, driver):
        cookie_file_path = os.path.join(self.cookie_folder, self.cookie_name) + ".pkl"
        if os.path.isfile(cookie_file_path):
            self.load(driver, self.BASE_URL, self.cookie_name)
            driver.get(self.BASE_URL)
            if not self.get_sign_in_button(driver):
                return driver, True
        return driver, False

    def start(self, driver: WebDriver) -> bool:
        action = ActionChains(driver)
        driver.get(self.BASE_URL)
        self.please_update_your_browser(driver)
        driver, success = self.login_cookies(driver)
        SUCCESS_C = f"[C] {self.email} logged in successfully!"
        SUCCESS_P = f"[P] {self.email} logged in successfully!"
        FAILURE = f"[!] {self.email} failed to log in!"
        if success:
            logger.success(SUCCESS_C)
            return True
        else:
            signin = self.get_sign_in_button(driver)
            action.move_to_element(signin).click().perform()
            success = self.credentials(driver)
            if success:
                logger.success(SUCCESS_P)
                return True
        logger.error(FAILURE)
        return False
