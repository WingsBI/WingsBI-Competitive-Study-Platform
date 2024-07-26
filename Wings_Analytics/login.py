# login.py
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wings_login(driver, email, password):
    driver.get("https://analytics.wingsbi.com/")
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='Log in'])[1]"))
    )
    login_button.click()
    
    email_field = driver.find_element(By.ID, "email")
    email_field.send_keys(email)
    
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys(password)
    
    signin_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type=submit]"))
    )
    signin_button.click()
    
    time.sleep(5)
