import json
import os

# Load the parsed data from the JSON file
file_name = "parsed_data.json"
json_file_path = os.path.join(os.getcwd(), file_name)

with open(json_file_path, "r") as json_file:
    parsed_data = json.load(json_file)

# Initialize counters for different categories
total_points = 0
points_without_lat_lon_but_with_postal = 0
points_with_lat_lon_but_no_postal = 0
points_with_lat_lon_and_postal = 0
points_with_no_lat_lon_or_postal = 0

# Iterate through the parsed data and calculate statistics
for point in parsed_data:
    total_points += 1
    latitude = point["latitude"]
    longitude = point["longitude"]
    postal_code = point["postal_code"]

    if latitude == "N/A" and longitude == "N/A" and postal_code != "N/A":
        points_without_lat_lon_but_with_postal += 1
    elif (latitude != "N/A" or longitude != "N/A") and postal_code == "N/A":
        points_with_lat_lon_but_no_postal += 1
    elif (latitude != "N/A" and longitude != "N/A") and postal_code != "N/A":
        points_with_lat_lon_and_postal += 1
    else:
        points_with_no_lat_lon_or_postal += 1

# Print the statistics
print("Total number of points:", total_points)
print("Number of points without latitude and longitude but with postal code:", points_without_lat_lon_but_with_postal)
print("Number of points with latitude and longitude but no postal code:", points_with_lat_lon_but_no_postal)
print("Number of points with latitude and longitude and postal code:", points_with_lat_lon_and_postal)
print("Number of points with no latitude, longitude, and postal code:", points_with_no_lat_lon_or_postal)
