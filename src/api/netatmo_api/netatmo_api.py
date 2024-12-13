import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

class NetatmoAPI:
    def __init__(self):
        # Load credentials and tokens from environment variables
        self.access_token = os.getenv("NETATMO_ACCESS_TOKEN")

        if not self.access_token:
            raise ValueError("Environment variable NETATMO_ACCESS_TOKEN must be set.")

    def get_home_data(self):
        """Retrieve home data from the Netatmo API."""
        endpoint = "https://api.netatmo.com/api/homesdata"
        headers = {"Authorization": f"Bearer {self.access_token}"}

        response = requests.get(endpoint, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch home data: {response.json()}")

if __name__ == "__main__":
    # Initialize the API client
    netatmo = NetatmoAPI()

    try:
        # Fetch home data
        home_data = netatmo.get_home_data()
        print("Home Data written to file: home_data.json")

        # Write to a file
        with open("src/api/netatmo_api/home_data.json", "w") as file:
            json.dump(home_data, file, indent=4)

    except Exception as e:
        print("Error:", e)
