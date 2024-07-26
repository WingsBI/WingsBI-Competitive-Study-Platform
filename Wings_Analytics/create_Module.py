# add_new_question.py
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def add_new_question(driver, question):
    try:
        wings_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[3]/div[3]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]"))
        )
        wings_input.click()
        wings_input.send_keys(Keys.CONTROL + "a")
        wings_input.send_keys(Keys.DELETE)
        driver.execute_script("arguments[0].value = '';", wings_input)
        wings_input.send_keys(question)
        wings_input.send_keys(Keys.RETURN)
        time.sleep(5)
    except Exception as e:
        print(f"Error asking Wings: {str(e)}")

    try:
        generate_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='Generate'])[1]"))
        )
        generate_button.click()
        time.sleep(10)
    except TimeoutException:
        print("Timeout occurred while waiting for the button to be clickable.")
    except Exception as e:
        print(f"An error occurred: {e}")
