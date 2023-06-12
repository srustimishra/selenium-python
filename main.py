import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
time.sleep(3)

# Go to webpage
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(2)

# Type username student into Username field
username_locator = driver.find_element(By.ID, "username")
username_locator.send_keys("student")

# Type password Password123 into Password field
password_locator = driver.find_element(By.NAME, "password")
password_locator.send_keys("Password123")

# Push Submit button
submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
submit_button_locator.click()
time.sleep(2)

actual_url = driver.current_url
assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"

logged_successfully = driver.find_element(By.TAG_NAME, "h1")
actual_text = logged_successfully.text
assert actual_text == "Logged In Successfully"

logout_btn = driver.find_element(By.LINK_TEXT, "Log out")
logout_btn.click();

driver.close()
driver.quit()
