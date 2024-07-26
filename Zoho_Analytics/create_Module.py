# ask_zia.py
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def ask_zia(driver, question):
    try:
        zia_icon = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[10]/div[4]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/ul[1]/li[6]"))
        )
        driver.execute_script("arguments[0].click();", zia_icon)
        
        zia_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[10]/div[4]/table[1]/tbody[1]/tr[1]/td[3]/table[1]/tbody[1]/tr[2]/td[3]/div[2]/div[1]/div[1]/div[2]/span[1]/div[1]/div[1]/textarea[1]"))
        )
        zia_input.click()
        zia_input.send_keys(question)
        time.sleep(2)
        zia_input.send_keys(Keys.RETURN)
        time.sleep(5)
    except Exception as e:
        print(f"Error asking Zia: {str(e)}")
