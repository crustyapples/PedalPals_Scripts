import requests
from auth import get_access_token
import config 

query_name = "bicyclerack"

token,expiry_timestamp = get_access_token(config.EMAIL, config.PASSWORD)

url = f"https://www.onemap.gov.sg/api/public/themesvc/retrieveTheme?queryName={query_name}"
      
headers = {"Authorization": f"{token}"}
      
response = requests.request("GET", url, headers=headers)

data = response.json()

for item in data["SrchResults"]:
    print(item)