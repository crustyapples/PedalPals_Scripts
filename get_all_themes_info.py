import requests
from auth import get_access_token
      
url = "https://www.onemap.gov.sg/api/public/themesvc/getAllThemesInfo?moreInfo=Y"
token,expiry_timestamp = get_access_token(config.EMAIL, config.PASSWORD)

headers = {"Authorization": f"{token}"}
      
try:
    response = requests.request("GET", url, headers=headers)
    response.raise_for_status()
    data = response.json()
    theme_names = set()

    for item in data['Theme_Names']:
        theme_names.add((item['CATEGORY'],item['THEMENAME'],item['QUERYNAME']))

    # sort through theme_names by theme_names[0]
    theme_names = sorted(theme_names, key=lambda x: x[0])

    for item in theme_names:        print(item)


except requests.exceptions.HTTPError as errh:
    print("HTTP Error:", errh)
except requests.exceptions.ConnectionError as errc:
    print("Error Connecting:", errc)
except requests.exceptions.Timeout as errt:
    print("Timeout Error:", errt)
except requests.exceptions.RequestException as err:
    print("Something went wrong:", err)
