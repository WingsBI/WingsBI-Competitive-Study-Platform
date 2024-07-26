# login.py
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def zoho_login(driver, email, password):
    driver.get("https://analytics.zoho.com/")
    
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "SIGN IN")]'))
    )
    login_button.click()

    email_field = driver.find_element(By.ID, 'login_id')
    email_field.send_keys(email)
    email_field.send_keys(Keys.RETURN)
    
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'password'))
    )
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)
    
    try:
        i_understand_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[1]/a'))
        )
        i_understand_button.click()
    except:
        print("Login successful but 'I Understand' button not found.")
