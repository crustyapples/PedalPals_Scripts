import requests
import googlemaps
import folium
from auth import get_access_token
import config

# Function to make the OneMap API request and plot the route on a map
def plot_onemap_route(start, end):
    url = f"https://www.onemap.gov.sg/api/public/routingsvc/route?start={start}&end={end}&routeType=cycle"
    token, expiry_timestamp = get_access_token(config.EMAIL, config.PASSWORD)

    headers = {"Authorization": f"{token}"}

    response = requests.get(url, headers=headers)
    data = response.json()

    # Extract route geometry
    route_geometry = data.get("route_geometry", "")

    if route_geometry:
        # Decode the polyline
        decoded_route = googlemaps.convert.decode_polyline(route_geometry)

        # Extract coordinates (lat, lng) from the list of dictionaries
        coordinates = [(point['lat'], point['lng']) for point in decoded_route]

        # Create a folium map
        route_map = folium.Map(location=coordinates[0], zoom_start=15)

        # Plot the OneMap route on the map
        folium.PolyLine(locations=coordinates, color='red').add_to(route_map)

        # Save the map
        route_map.save("onemap_route_map.html")
        print("OneMap route map saved as onemap_route_map.html")

# Function to make the Google Maps API request and plot the route on a map
def plot_google_maps_route(start, end):
    # Initialize the Google Maps client
    gmaps = googlemaps.Client(key=config.GOOGLE_MAPS_API)

    # Request directions with traffic information
    directions_result = gmaps.directions(
        start,
        end,
        mode="bicycling",
        departure_time="now",
        traffic_model="best_guess",
    )

    if not directions_result:
        print("No directions found.")
        return

    # Extract the route steps and overview polyline
    route = directions_result[0]
    overview_polyline = route["overview_polyline"]["points"]

    # Decode the polyline
    decoded_route = googlemaps.convert.decode_polyline(overview_polyline)

    # Extract coordinates (lat, lng) from the list of dictionaries
    coordinates = [(point['lat'], point['lng']) for point in decoded_route]

    # Create a folium map
    route_map = folium.Map(location=coordinates[0], zoom_start=15)

    # Plot the Google Maps route on the map
    folium.PolyLine(locations=coordinates, color='blue').add_to(route_map)

    # Save the map
    route_map.save("google_maps_route_map.html")
    print("Google Maps route map saved as google_maps_route_map.html")

# Coordinates for the route
start_coords = "1.3177824,103.932945"
end_coords = "1.341815,103.8360822"

# Call the function to plot the route on a map
plot_onemap_route(start_coords, end_coords)
plot_google_maps_route(start_coords, end_coords)
