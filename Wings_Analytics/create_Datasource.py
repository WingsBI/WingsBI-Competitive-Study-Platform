# select_datasource.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def select_datasource(driver):
    try:
        dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@role='combobox']"))
        )
        dropdown.click()
        options = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[4]/div[3]/ul/li[2]'))
        )
        for option in options:
            if option.text == "insurance":
                option.click()
                break
    except Exception as e:
        print(f"An error occurred while selecting datasource from dropdown: {e}")
