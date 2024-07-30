# capture_screenshot_and_save.py
import os
import pyautogui

def zoho_capture_screenshot(question, driver):
    try:
        # Get the directory of the current script
        script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        # Define the folder path as the script directory
        zoho_folder = os.path.join(script_dir, 'Screenshots','Zoho_Analytics_Sc')
        
        # Create the screenshots directory if it does not exist
        os.makedirs(zoho_folder, exist_ok=True)

        # Define the filename based on the question
        filename = f"{question[:].replace('?', '_')}.png"
        screenshot_file = os.path.join(zoho_folder, filename)

        # Take and save the screenshot
        screenshot = pyautogui.screenshot()
        screenshot.save(screenshot_file)
        driver.refresh()
    except Exception as e:
        print(f"An error occurred while capturing and saving screenshot: {e}")
