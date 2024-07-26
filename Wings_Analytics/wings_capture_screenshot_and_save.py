# capture_screenshot_and_save.py
import os
import pyautogui

def wings_capture_screenshot(folder_path, question):
    try:
        os.makedirs(folder_path, exist_ok=True)
        filename = f"{question[:].replace('?', '_')}.png"
        screenshot_file = os.path.join(folder_path, filename)
        screenshot = pyautogui.screenshot()
        screenshot.save(screenshot_file)
    except Exception as e:
        print(f"An error occurred while capturing and saving screenshot: {e}")
