import xml.etree.ElementTree as ET
import json
import re
import os

# Load the KML file
file_name = "water.kml"
print(os.getcwd())
kml_file = os.path.join(os.getcwd(), file_name)

# i want to get the file path dynamically


tree = ET.parse(kml_file)
root = tree.getroot()

# Initialize a list to store parsed data
parsed_data = []

# Find all Placemark elements
placemarks = root.findall(".//{http://www.opengis.net/kml/2.2}Placemark")

# Function to check and fix coordinates
def fix_coordinates(latitude, longitude):
    try:
        # Convert coordinates to float
        latitude = float(latitude)
        longitude = float(longitude)

        # Check if coordinates are within valid ranges
        if -90.0 <= latitude <= 90.0 and -180.0 <= longitude <= 180.0:
            return latitude, longitude
    except ValueError:
        pass  # Invalid coordinates

    # If coordinates are invalid, set them to N/A
    return "N/A", "N/A"

# Function to extract coordinates, Postal Code, and Description from description field using regex
def extract_info(description):
    latitude_match = re.search(r'Latitude::\s*([-+]?\d+\.\d+)', description)
    longitude_match = re.search(r'Longitude::\s*([-+]?\d+\.\d+)', description)
    postal_code_match = re.search(r'Postal Code::\s*([\w\d\s]+)', description)
    
    # Modify the regex pattern to account for <br> tag before Description
    description_match = re.search(r'1<br>\s*Description::\s*([^<]+)', description)

    latitude = latitude_match.group(1) if latitude_match else "N/A"
    longitude = longitude_match.group(1) if longitude_match else "N/A"
    postal_code = postal_code_match.group(1) if postal_code_match else "N/A"
    description_text = description_match.group(1) if description_match else "N/A"

    return latitude, longitude, postal_code, description_text  # Include the description_text in the return value



# Iterate through each Placemark and extract details
for placemark in placemarks:
    info = {}
    name_element = placemark.find(".//{http://www.opengis.net/kml/2.2}name")
    info["name"] = name_element.text if name_element is not None else ""

    description_element = placemark.find(".//{http://www.opengis.net/kml/2.2}description")
    info["data"] = description_element.text if description_element is not None else ""

    # Initialize latitude, longitude, postal code, and description as N/A
    latitude = "N/A"
    longitude = "N/A"
    postal_code = "N/A"
    description_text = "N/A"

    if info["data"]:
        # Extract coordinates, Postal Code, and Description from description using regex
        latitude, longitude, postal_code, description_text = extract_info(info["data"])

    # Fix coordinates if needed
    fixed_latitude, fixed_longitude = fix_coordinates(latitude, longitude)

    info["latitude"] = fixed_latitude
    info["longitude"] = fixed_longitude
    info["postal_code"] = postal_code
    info["description_text"] = description_text  # Include the extracted description

    parsed_data.append(info)


# Save parsed data to a JSON file

json_file_path = os.path.join(os.getcwd(), "parsed_data.json")
with open(json_file_path, "w") as json_file:
    json.dump(parsed_data, json_file, indent=2)

print("Parsed data saved to parsed_data.json")
