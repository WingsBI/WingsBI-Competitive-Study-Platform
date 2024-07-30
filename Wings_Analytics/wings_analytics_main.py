# wings_analytics_main.py
import time
import pandas as pd
from selenium import webdriver
from Wings_Analytics.wings_capture_screenshot_and_save import wings_capture_screenshot
from Wings_Analytics.create_Datasource import select_datasource
from Wings_Analytics.create_Module import add_new_question
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from Wings_Analytics.login import wings_login

def execute(email, password, questions_df):
    driver = initialize_driver()
    wings_login(driver, email, password)
    navigate_to_modules(driver)
    select_datasource(driver)
    
    questions = questions_df.iloc[:, 1].dropna().tolist()
    for question in questions:
        add_new_question(driver, question)
        time.sleep(5)
        wings_capture_screenshot(question)
        time.sleep(3)

    driver.quit()

def initialize_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver

def navigate_to_modules(driver):
    modules = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//img[@class='css-1b3ssc6-menuIcons'])[3]"))
    )
    modules.click()

    add_new = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiCard-root css-1vip7m1'])[1]"))
    )
    add_new.click()
