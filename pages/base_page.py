from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver, timeout=5):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)

    def find(self, locator: tuple[str, str]):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator: tuple[str, str]):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator: tuple[str, str], value: str):
        self.find(locator).clear()
        self.find(locator).send_keys(value)

    def get_text(self, locator: tuple[str, str]):
        return self.find(locator).text

    def is_text_present(self, locator: tuple[str, str], text: str) -> bool:
        try:
            return self.wait.until(EC.text_to_be_present_in_element(locator, text))
        except TimeoutException:
            return False

    def is_visible(self, locator: tuple[str, str]) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
