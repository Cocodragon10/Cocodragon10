import time
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#pip install webdriver-manager

# CONFIG
URL = "https://moodle.tktk.ee/"
USERNAME = "nimi"
TEST_COUNT = 5

#1: Gen password
def generate_password():
    length = random.randint(5, 12)
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))

#2: login test
def perform_login(browser, wait, username, password_value):
    browser.get(URL)

    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Log in"))).click()

    time.sleep(1.5)

    user_field = wait.until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    user_field.clear()
    user_field.send_keys(username)

    time.sleep(1.5)

    pass_field = wait.until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    pass_field.clear()
    pass_field.send_keys(password_value)

    time.sleep(1)

    login_btn = wait.until(
        EC.element_to_be_clickable((By.ID, "loginbtn"))
    )
    login_btn.click()

#3 tests
def run_tests():
    browser = webdriver.Chrome()
    wait = WebDriverWait(browser, 10)

    results = []

    for i in range(TEST_COUNT):
        test_password = generate_password()

        print(f"\nTest {i + 1}")
        print(f"Password: {test_password}")

        try:
            perform_login(browser, wait, USERNAME, test_password)
            time.sleep(2)

            results.append((test_password, "Jah"))

        except Exception as e:
            results.append((test_password, f"Mis juhtus: {str(e)}"))

        time.sleep(2)

    browser.quit()
    return results

# MAIN
if __name__ == "__main__":
    results = run_tests()
#GPT
    print("\n Resultt")
    for password, status in results:
        print(f"{password} -> {status}")