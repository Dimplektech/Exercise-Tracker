"""
Exercise Tracker Script

This script allows you to log your daily exercises by integrating with the Nutritionix API
to calculate calories burned based on your input and personal details (age, gender, weight, height).
The results are then stored in a Google Sheet via the Sheety API.

The script works as follows:

1. User is prompted to input the type of exercise they performed.
2. Nutritionix API is used to calculate details such as duration and calories burned.
3. The exercise data (name, duration, calories) is logged to a Google Sheet using the Sheety API.

Requirements:
- Environment variables:
    - `API_KEY`: API key for Nutritionix API.
    - `APP_ID`: Application ID for Nutritionix API.
    - `EXERCISE_ENDPOINT`: URL endpoint for Nutritionix API (exercise).
    - `SHEETY_ENDPOINT`: URL endpoint for Sheety API (Google Sheet integration).
    - `SHEETY_USER`: Username for HTTP Basic Authentication with Sheety API.
    - `SHEETY_PASSWO`: Password for HTTP Basic Authentication with Sheety API.

Key Modules:
- `requests`: For handling HTTP requests to the APIs.
- `datetime`: For handling date and time formatting.
- `os`: For retrieving environment variables.
- `requests.auth.HTTPBasicAuth`: For handling basic authentication with the Sheety API.

How to use:
1. Ensure that your environment variables are properly set.
2. Run the script using 'python main.py' on  command line, input the exercise activity,
   and the data will be logged into the Google Sheet.

"""

import requests # To handle API requests
from datetime import datetime # To handle date and time formatting
from requests.auth import HTTPBasicAuth # For basic authentication with Sheety API
import os # To retrieve environment variables

# Personal information for exercise tracking
GENDER = "female"
WEIGHT_KG = "57"
HEIGHT_CM ="160"
AGE = 30

# Get API keys and endpoints from environment variables
API_KEY = os.environ.get("API_KEY")  # Nutritionix API key
APPLICATION_ID = os.environ.get("APP_ID") # Nutritionix Application ID

# Get Sheety and Nutritionix API endpoints
sheety_endpoint = os.environ.get("SHEETY_ENDPOINT") # Endpoint to Google Sheet via Sheety
exercise_endpoint = os.environ.get("EXERCISE_ENDPOINT") # Endpoint for Nutritionix exercise API

# Prompt the user to input their exercise
exercise_text = input("Tell me which exercise you did:")

# Define headers to authenticate with Nutritionix API
headers = {
    "x-app-id":APPLICATION_ID, # Application ID for Nutritionix API
    "x-app-key":API_KEY # API key for Nutritionix API
}

# Set the parameters to be sent in the API request, including user details and the exercise query
params = {
    "query":exercise_text,
    "gender":GENDER,
    "weight_kg":WEIGHT_KG,
    "height_cm":HEIGHT_CM,
    "age":AGE

}

# Send a POST request to the Nutritionix API with the exercise details
response = requests.post(exercise_endpoint,json=params,headers=headers)

# Parse the JSON response from the Nutritionix API
result = response.json()
print(result)

# Get today's date and the current time to log with the exercise data
today_date = datetime.now().strftime("%d/%m/%Y") # Format date as Day/Month/Year
now_time = datetime.now().strftime("%X") # Format time as HH:MM:SS

# Get Sheety credentials for HTTP Basic Authentication from environment variables
user = os.environ.get("SHEETY_USER")  # Sheety username
password = os.environ.get("SHEETY_PASSWO") # Sheety password

# Set up basic authentication for Sheety API
basic = HTTPBasicAuth(user, password)

# Loop through each exercise returned by the Nutritionix API
for exercise in result["exercises"]:
    # Create a dictionary with the data to be logged in the Google Sheet
    sheet_inputs = {
        "workout":{
            "date":today_date,
            "time":now_time,
            "exercise":exercise["name"].title(),
            "duration":exercise["duration_min"],
            "calories":exercise["nf_calories"]

        }

    }
    # Send a POST request to the Sheety API to log the exercise data in the Google Sheet
    sheet_response = requests.post(sheety_endpoint, json=sheet_inputs,auth=basic)
    # Print the response from the Sheety API (for debugging or confirmation)
    print(sheet_response.text)





