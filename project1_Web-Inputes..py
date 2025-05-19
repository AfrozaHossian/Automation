import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# Start Browser session
driver = webdriver.Firefox()
driver.maximize_window()

driver.implicitly_wait(10)

driver.get("https://practice.expandtesting.com/inputs")

# Enter/Type Number
test_number = "123456"
input_number = driver.find_element(by=By.ID, value="input-number")
input_number.send_keys(test_number)

# Enter/Type Text
test_text = "abcd"
input_text = driver.find_element(by=By.ID, value="input-text")
input_text.send_keys(test_text)

# Enter/Type Password

test_password = "abcd@1234"
input_password = driver.find_element(by=By.ID, value="input-password")
input_password.send_keys(test_password)
print(test_password)

# Enter/Type Date

test_date = "2025-05-11"
input_date = driver.find_element(by=By.ID, value="input-date")
input_date.send_keys(test_date)
print(test_date)


# Display button
display_button = driver.find_element(by=By.ID, value="btn-display-inputs")
display_button.click()

# start Verify number

try:
    output_number = driver.find_element(by=By.ID, value="output-number")

    try:
        display_number = output_number.text
        assert display_number == test_number
        print("Number Assertion Passed.")
    except AssertionError:
        print("Assertion Failed. Input and Output text Mismatch.")
    except Exception as e:
        print(f"Error Occurred: {e}")

except Exception as e:
    print(f"Number field did not found.Exception: {e}")

#close Verify number


# Verify text

try:
    output_text = driver.find_element(by=By.ID, value="output-text")

    try:
        display_text = output_text.text
        assert display_text == test_text
        print("Text Assertion Passed.")
    except AssertionError:
        print("Assertion Failed. Input and Output text Mismatch.")
    except Exception as e:
        print(f"Error Occurred: {e}")

except Exception as e:
    print(f"Text field did not found.Exception: {e}")





# Verify Password

try:
    output_password = driver.find_element(by=By.ID, value="output-password")

    try:
        display_password = output_password.text
        assert display_password == test_password
        print("Password Assertion Passed.")
    except AssertionError:
        print("Assertion Failed. Input and Output Password Mismatch.")
    except Exception as e:
        print(f"Error Occurred: {e}")

except Exception as e:
    print(f"Number field did not found.Exception: {e}")

#close Password

# Verify Date

try:
    output_date = driver.find_element(by=By.ID, value="output-date")

    try:
        display_date = output_date.text
        assert display_date == test_date
        print("Date Assertion Passed.")
    except AssertionError:
        print("Assertion Failed. Input and Output Date Mismatch.")
    except Exception as e:
        print(f"Error Occurred: {e}")

except Exception as e:
    print(f"Number field did not found.Exception: {e}")

# Date close
print("Test Complete")
driver.quit()