# zoho_analytics_main.py
import time
from Zoho_Analytics.create_Module import ask_zia
from Zoho_Analytics.login import zoho_login
from Zoho_Analytics.zoho_capture_screenshot_and_save import zoho_capture_screenshot

def zoho_execute(email, password, questions_df):
    driver = initialize_driver()
    zoho_login(driver, email, password)
    
    questions = questions_df.iloc[:, 1].dropna().tolist()
    for question in questions:
        ask_zia(driver, question)
        time.sleep(5)
        zoho_capture_screenshot(question, driver)
        time.sleep(3)

    driver.quit()

# initialize_driver.py
from selenium import webdriver

def initialize_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver
