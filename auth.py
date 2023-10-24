import requests

def get_access_token(email, password):
    url = "https://www.onemap.gov.sg/api/auth/post/getToken"

    payload = {
        "email": email,
        "password": password
    }

    # Make a POST request with JSON payload
    response = requests.post(url, json=payload)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract the access_token and expiry_timestamp
        access_token = data.get("access_token")
        expiry_timestamp = data.get("expiry_timestamp")

        return access_token, expiry_timestamp
    else:
        # Print an error message if the request was not successful
        print("Request failed with status code:", response.status_code)
        print("Response content:", response.text)