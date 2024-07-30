#main.py
import pandas as pd
import time
import os
import csv
from tkinter import Tk, filedialog
from PPT_Generation.ppt_script import create_presentation
from Wings_Analytics.wings_analytics_main import execute
from Zoho_Analytics.zoho_analytics_mains import zoho_execute

# Initialize Tkinter and hide the main window
root = Tk()
root.withdraw()

# Ask user to select CSV file
csv_file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

# Check if a file was selected
if not csv_file_path:
    print("No file selected. Exiting...")
    exit()

# Read CSV file using pandas with 'latin-1' encoding
questions_df = pd.read_csv(csv_file_path, encoding='latin-1')

# Extract email and password for Wings and Zoho
wings_email = questions_df.iloc[0, 5]  # Assuming column B contains email
wings_password = questions_df.iloc[0, 6]  # Assuming column C contains password
zoho_email = questions_df.iloc[1, 5]  # Assuming column B contains email
zoho_password = questions_df.iloc[1, 6]  # Assuming column C contains password

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define common folder paths as subdirectories of the script directory
wings_folder = os.path.join(script_dir, 'Screenshots','Wings_Analytics_Sc')
zoho_folder = os.path.join(script_dir,  'Screenshots','Zoho_Analytics_Sc')

# Run Wings Analytics
wings_Analytics = execute(wings_email, wings_password, questions_df)

# Run ZOho Analytics
zoho_Analytics = zoho_execute(zoho_email, zoho_password, questions_df)

# Run PPT
ppt_Generation = create_presentation(csv_file_path, wings_folder, zoho_folder, questions_df)
 