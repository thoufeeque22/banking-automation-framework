# tests/registration_test.py
import allure
import pytest

from pages.registration_page import RegistrationPage


@allure.feature("User Registration")
@allure.story("Successful new user registration")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.registration
def test_user_registration(setup_browser, user):
    driver = setup_browser
    reg_page = RegistrationPage(driver)

    with allure.step("Open the Registration Page"):
        reg_page.go_to_registration_page()

    with allure.step("Fill out the registration form"):
        reg_page.register(
            first_name=user["first_name"],
            last_name=user["last_name"],
            street=user["street"],
            city=user["city"],
            state=user["state"],
            zip=user["zip"],
            phone=user["phone"],
            ssn=user["ssn"],
            username=user["username"],
            password=user["password"],
        )

    with allure.step("Verify registration success message"):
        assert reg_page.is_text_present(
            reg_page.welcome_text_el, f"Welcome {user['username']}"
        ), f"Expected welcome text not found for user {user['username']}"
        assert reg_page.is_text_present(
            reg_page.acc_created_text_el, "You are now logged in."
        ), "Account creation confirmation text missing"
