# Exercise-Tracker


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

### 1. **Clone the Repository**
    
    To get started, first, clone this repository to your local machine:
    
    ```bash
    git clone https://github.com/Dimplektech/Exercise-Tracker.git

### 2. **Create a Virtual Environment (Optional but Recommended)
  Creating a virtual environment isolates your project and helps manage dependencies. To set up a virtual environment:
    # Create a virtual environment
     ```bash
     python -m venv venv
    
    # Activate the virtual environment
    # On Windows
     ```bash
    venv\Scripts\activate
    
    # On macOS/Linux
     ```bash
    source venv/bin/activate


