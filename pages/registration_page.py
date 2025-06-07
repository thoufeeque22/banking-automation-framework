# pages/registration_data.py
import os
import traceback

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from utils import common_functions
from utils import logger
from .base_page import BasePage


class RegistrationPage(BasePage):
    URL = "https://parabank.parasoft.com/parabank/register.htm"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.logger = logger.setup_logger(self.__class__.__name__)
        self.driver = driver
        self.firstname_input = (By.CSS_SELECTOR, "[id='customer.firstName']")
        self.lastname_input = (By.CSS_SELECTOR, "[id='customer.lastName']")
        self.street_input = (By.CSS_SELECTOR, "[id='customer.address.street']")
        self.city_input = (By.CSS_SELECTOR, "[id='customer.address.city']")
        self.state_input = (By.CSS_SELECTOR, "[id='customer.address.state']")
        self.zip_input = (By.CSS_SELECTOR, "[id='customer.address.zipCode']")
        self.phone_input = (By.CSS_SELECTOR, "[id='customer.phoneNumber']")
        self.ssn_input = (By.CSS_SELECTOR, "[id='customer.ssn']")
        self.username_input = (By.CSS_SELECTOR, "[id='customer.username']")
        self.password_input = (By.CSS_SELECTOR, "[id='customer.password']")
        self.repeat_pw_input = (By.CSS_SELECTOR, "[id='repeatedPassword']")
        self.register_button = (By.CSS_SELECTOR, '[value="Register"]')
        self.welcome_text_el = (By.CSS_SELECTOR, ".title")
        self.acc_created_text_el = (By.CSS_SELECTOR, "#rightPanel p")

    def go_to_registration_page(self):
        self.driver.get(self.URL)

    def register(
        self,
        first_name: str,
        last_name: str,
        street: str,
        city: str,
        state: str,
        zip: str,
        phone: str,
        ssn: str,
        username: str,
        password: str,
    ):
        self.logger.info("Filling registration form")
        self.type(self.firstname_input, first_name)
        self.logger.debug(f"First name entered: {first_name}")
        self.type(self.lastname_input, last_name)
        self.logger.debug(f"Last name entered: {last_name}")
        self.type(self.street_input, street)
        self.logger.debug(f"street name entered: {street}")
        self.type(self.city_input, city)
        self.logger.debug(f"city name entered: {city}")
        self.type(self.state_input, state)
        self.logger.debug(f"state name entered: {state}")
        self.type(self.zip_input, zip)
        self.logger.debug(f"zip name entered: {zip}")
        self.type(self.phone_input, phone)
        self.logger.debug(f"phone name entered: {phone}")
        self.type(self.ssn_input, ssn)
        self.logger.debug(f"ssn name entered: {ssn}")
        self.type(self.username_input, username)
        self.logger.debug(f"username entered: {username}")
        self.type(self.password_input, password)
        self.logger.debug(f"password entered: {password}")
        self.type(self.repeat_pw_input, password)
        self.logger.debug(f"repeat password entered: {password}")
        self.click(self.register_button)
        self.logger.debug(f"register button clicked: {password}")
        self.logger.info("User registered successfully")
