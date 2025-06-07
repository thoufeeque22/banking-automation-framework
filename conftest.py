# conftest.py
import os
import tempfile
from datetime import datetime

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.common_functions import read_csv_data


@pytest.fixture(scope="function")
def setup_browser():
    chrome_options = Options()
    # Run headless on CI for stability & speed (optional)
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Create a unique temp dir for user data to avoid conflicts
    temp_user_data_dir = tempfile.mkdtemp()
    chrome_options.add_argument(f"--user-data-dir={temp_user_data_dir}")

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("setup_browser")
        if driver:
            # Base screenshots directory
            base_dir = os.path.abspath("reports/screenshots")

            # Create a directory named after the test function
            test_dir = os.path.join(base_dir, item.name)
            os.makedirs(test_dir, exist_ok=True)

            # Add timestamp to screenshot file name
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_name = f"{item.name}_{timestamp}.png"
            screenshot_path = os.path.join(test_dir, screenshot_name)

            driver.save_screenshot(screenshot_path)

            with open(screenshot_path, "rb") as image_file:
                allure.attach(image_file.read(), name="Failure Screenshot", attachment_type=allure.attachment_type.PNG)

def pytest_generate_tests(metafunc):
    if "user" in metafunc.fixturenames:

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        test_data_path = os.path.join(BASE_DIR, "data", "registration_data.csv")
        test_data = read_csv_data(test_data_path)
        metafunc.parametrize("user", test_data)
