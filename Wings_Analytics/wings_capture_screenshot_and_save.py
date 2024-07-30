# wings_capture_screenshots_and_save.py
import os
import pyautogui

def wings_capture_screenshot(question):
    try:
        # Get the directory of the current script
        script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        # Define the folder path as the script directory
        wings_folder = os.path.join(script_dir, 'Screenshots','Wings_Analytics_Sc')
        
        # Create the screenshots directory if it does not exist
        os.makedirs(wings_folder, exist_ok=True)
        
        # Define the filename based on the question
        filename = f"{question[:].replace('?', '_')}.png"
        screenshot_file = os.path.join(wings_folder, filename)
        
        # Take and save the screenshot
        screenshot = pyautogui.screenshot()
        screenshot.save(screenshot_file)
    except Exception as e:
        print(f"An error occurred while capturing and saving screenshot: {e}")
