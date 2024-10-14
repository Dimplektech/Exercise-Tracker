# Exercise Tracker

This Python script allows you to track your exercise activities by integrating with the **Nutritionix API** and the **Sheety API**. The script calculates the calories burned based on your personal data and logs the results in a Google Sheet.

## Features

- **Exercise Logging**: Enter details about the exercise you performed, and the script will use the Nutritionix API to calculate the calories burned.
- **Google Sheets Integration**: Automatically logs the exercise details (name, duration, calories burned) into a Google Sheet using the Sheety API.
- **Personalized Data**: The calculation is based on your gender, weight, height, and age for more accurate results.

---

## Prerequisites

Before you can use this script, ensure you have the following:

1. **Nutritionix Account**: Create an account and generate your API key [here](https://www.nutritionix.com/business/api).
2. **Sheety Account**: Create a Google Sheet and use Sheety to generate an API endpoint [here](https://sheety.co/).
3. **Python Environment**: You'll need Python installed on your machine (version 3.x recommended).

---

## Setting Up Your Environment

### 1. Clone the Repository
    
To get started, first, clone this repository to your local machine:
  git clone https://github.com/Dimplektech/Exercise-Tracker.git
  

### 2. Create a Virtual Environment (Optional but Recommended)
 - Creating a virtual environment isolates your project and helps manage dependencies. To set up a virtual environment:
     Create a virtual environment
     
     
     python -m venv venv
    
 - Activate the virtual environment **
   #### On Windows
        
        venv\Scripts\activate
   
   #### On macOS/Linux
       
       source venv/bin/activate

### 3. Install Dependencies
 Install the required Python packages using pip:    
    pip install -r requirements.txt

### 4. Setting Up Environment Variables
You need to set up several environment variables to securely pass API keys and endpoints to the script. Follow the steps below to configure them:
    
#### On Linux/Mac:
You can set environment variables by adding the following lines to your ~/.bashrc or ~/.zshrc file:
    
        export API_KEY="your_nutritionix_api_key_here"
        export APP_ID="your_nutritionix_app_id_here"
        export EXERCISE_ENDPOINT="https://trackapi.nutritionix.com/v2/natural/exercise"
        export SHEETY_ENDPOINT="your_sheety_endpoint_here"
        export SHEETY_USER="your_sheety_username_here"
        export SHEETY_PASSWO="your_sheety_password_here"
    
* After adding these lines, reload your terminal: *
        source ~/.bashrc  # or ~/.zshrc for Zsh

    
#### On Windows (PowerShell):
You can set environment variables in PowerShell by running:

    $env:API_KEY="your_nutritionix_api_key_here"
    $env:APP_ID="your_nutritionix_app_id_here"
    $env:EXERCISE_ENDPOINT="https://trackapi.nutritionix.com/v2/natural/exercise"
    $env:SHEETY_ENDPOINT="your_sheety_endpoint_here"
    $env:SHEETY_USER="your_sheety_username_here"
    $env:SHEETY_PASSWO="your_sheety_password_here"


### 6.Run the script:        
         python main.py

###  Dependencies
        - requests: For making HTTP requests to the Nutritionix and Sheety APIs.
        - datetime: For handling date and time formatting.
        - os: For reading environment variables.
        - requests.auth: For HTTP Basic Authentication with the Sheety API.

 - You can install these dependencies by running:
    ```bash
    pip install requests

- Alternatively, use the requirements.txt file:
    ```bash
    pip install -r requirements.txt

    

    

        








