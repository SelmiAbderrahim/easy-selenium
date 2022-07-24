import random
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from ...logger import logger
from ...driver.utils import Util
from ...cookies.cookies import Cookies
from ...common.funcs import send_keys_one_by_one

util = Util()
WORKING_DIRECTORY = os.getcwd()


class Login(Cookies):
    """
    Automate LinkedIn authentication.

    Args:
        email (str): The LinkedIn email address
        password (str): The LinkedIn password

    Returns:
        The return value. True for success, False otherwise
    """
    BASE_URL = "https://www.linkedin.com"

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.cookie_name = f"linkedin_{email}"
        self.cookie_folder = os.path.join(WORKING_DIRECTORY, "cookies")
        util.create_folder_if_not_exist(self.cookie_folder)

    def get_signin_link(self, driver):
        try:
            signin = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//a[contains(@class,'nav__button-secondary')]")
                )
            )
        except TimeoutException:
            signin = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//a[text()='Sign in']"))
            )
        try:
            return signin, None
        except Exception as error:
            return None, error

    def is_logged_in(self, driver):
        if (
            driver.current_url
            == "https://www.linkedin.com/error_pages/unsupported-browser.html"
        ):
            try:
                skip = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//a[@title= 'continue anyway']")
                    )
                )
            except TimeoutException:
                pass
            except Exception as error:
                logger.error(
                    """
                LinkedIn requires an updated browser to work, Please update yours:
                https://www.linkedin.com/error_pages/unsupported-browser.html
                """
                    + str(error)
                )
            else:
                ActionChains(driver).move_to_element(skip).click().perform()
        time.sleep(random.randint(1, 5))
        if "feed" not in driver.current_url:
            return False
        return True

    def credentials(self, driver):
        time.sleep(random.randint(1, 5))
        signin, error = self.get_signin_link(driver)
        if signin:
            ActionChains(driver).move_to_element(signin).click().perform()
        else:
            driver.get("https://www.linkedin.com/login")
        try:
            login_input = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, "session_key"))
            )
        except TimeoutException:
            login_input = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, "username"))
            )
        send_keys_one_by_one(login_input, self.email)
        time.sleep(random.randint(1, 5))
        try:
            password_input = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, "session_password"))
            )
        except TimeoutException:
            password_input = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, "password"))
            )
        send_keys_one_by_one(password_input, self.password)
        time.sleep(random.randint(1, 5))
        try:
            submit_button = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//button[@class= 'sign-in-form__submit-button']")
                )
            )
        except TimeoutException:
            submit_button = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//button[@aria-label= 'Sign in']")
                )
            )
        ActionChains(driver).move_to_element(submit_button).click().perform()
        time.sleep(random.randint(1, 3))
        if self.is_logged_in(driver):
            self.save(driver, self.BASE_URL, self.cookie_name)
            return driver, True
        return driver, False

    def welcome_back_password(self, driver):
        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//a[text()='Sign in']"))
            )
        except TimeoutException:
            pass
        else:
            try:
                password_input = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.ID, "password"))
                )
            except TimeoutException:
                password_input = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//input[@aria-label='Password']")
                    )
                )
            send_keys_one_by_one(password_input, self.password)

    def login_cookies(self, driver):
        cookie_file_path = os.path.join(self.cookie_folder, self.cookie_name) + ".pkl"
        if os.path.isfile(cookie_file_path):
            self.load(driver, self.BASE_URL, self.cookie_name)
            driver.get(self.BASE_URL)
            self.welcome_back_password(driver)
            if self.is_logged_in(driver):
                return driver, True
        return driver, False

    def start(self, driver):
        driver.get(self.BASE_URL)
        time.sleep(random.randint(1, 10))
        driver, success = self.login_cookies(driver)
        SUCCESS_C = f"[C] {self.email} logged in successfully!"
        SUCCESS_P = f"[P] {self.email} logged in successfully!"
        FAILURE = f"[!] {self.email} failed to log in!"
        if success:
            logger.success(SUCCESS_C)
            return True
        else:
            driver, success = self.credentials(driver)
            if success:
                logger.success(SUCCESS_P)
                return True
        logger.error(FAILURE)
        return False
