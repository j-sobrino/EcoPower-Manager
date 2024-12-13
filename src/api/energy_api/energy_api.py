import os
from dotenv import load_dotenv
import requests
import json  # Import json module for pretty-printing

# Load environment variables from .env file
load_dotenv()

# URL for the consumption data
url = "https://monitorizacion.iberdrola.com/site/consumption/livesolarflow/23BacSVvnBRiapJGQXYkosxPmHCjMdKv8lQY8V1IbuU=/false/false"

# Retrieve sensitive data from .env
cookies = os.getenv("IBERDROLA_COOKIES")

# Ensure cookies are set
if not cookies:
    raise ValueError("Environment variable 'IBERDROLA_COOKIES' not set!")

# Headers
headers = {
    "Accept": "application/json",
    "Cookie": cookies,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Referer": "https://monitorizacion.iberdrola.com/site",
}

# Send GET request
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()

    # Pretty-print the JSON data
    print("Full JSON Response:")
    print(json.dumps(data, indent=4))  # Pretty-print the full JSON response

    consumption = data.get("data", {}).get("consumption", None)
    print(f"Current Consumption: {consumption} W")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
    print(response.text)
