email = input("Enter your Email: ")

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Start Browser session
driver = webdriver.Firefox()
driver.maximize_window()

driver.implicitly_wait(10)
driver.get("https://practice.expandtesting.com/forgot-password")

try:
    useremail = driver.find_element(by=By.ID, value="email")
    try:
        useremail.send_keys(email)
    except Exception as e:
        print(f"Error Occurred: {e}")
except Exception as e:
    print(f"username field did not found.Exception: {e}")



#  Retrieve password Button
try:
    login_button = driver.find_element(by=By.CSS_SELECTOR, value="button[type='submit']")


    #print("login button: ")
    #print(login_button)
    try:
        login_button.click()
    except Exception as e:
         print(f"Error Occurred: {e}")
except Exception as e:
    print(f"Login Button did not found.Exception: {e}")

# Verify Retrieve password



# Verify Login Successfully
try:
    flash = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "div[role='alert']")
        )
    )
    assert flash.text == "An e-mail has been sent to you which explains how to reset your password."
    print("Flash Message Found:", flash.text)
except AssertionError:
    print("Please enter a valid email address.")
except Exception as e:
     print("Please enter a valid email address")
    #print(f"Error Occurred: {e}")

driver.quit()