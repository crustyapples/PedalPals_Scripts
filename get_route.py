import requests
from auth import get_access_token
import config

# Function to make the API request
def get_route(start, end):
    url = f"https://www.onemap.gov.sg/api/public/routingsvc/route?start={start}&end={end}&routeType=cycle"
    token, expiry_timestamp = get_access_token(config.EMAIL, config.PASSWORD)


    headers = {"Authorization": f"{token}"}

    response = requests.get(url, headers=headers)
    data = response.json()

    print(data)  # Print the response data

# Coordinates for the route
start_coords = "1.3525545,103.6810534"
end_coords = "1.3203597,103.9378409"
# Call the function to get the route information
get_route(start_coords, end_coords)
