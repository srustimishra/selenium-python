import time
import pytest
from selenium.webdriver.common.by import By


@pytest.mark.datadriven
@pytest.mark.parametrize("username,password,expected_error_message",
                         [("Incorrectuser", "Password123", "Your username is invalid!"),
                          ("Incorrectuser2", "IncorrectPassword", "Your username is invalid!")])
class TestNegativeScenarios:
    def test_negative_username(self, driver,username,password,expected_error_message):
        # login_page=LoginPage(driver)
        # login_page.open()
        # login_page.execute_login()
        # assert login_page.get_error_message() == expected_error_message,"Error Message is not expected"
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type username incorrectUser into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys(username)

        # Type password Password123 into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys(password)

        # Push Submit button
        submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_button_locator.click()
        time.sleep(2)

        # Verify error message is displayed
        error_message_locator = driver.find_element(By.ID, "error")
        assert error_message_locator.is_displayed(), "Error message is not displayed, but it should be"

        # Verify error message text is Your username is invalid!
        error_message = error_message_locator.text
        assert error_message == expected_error_message, "Error message is not expected"

