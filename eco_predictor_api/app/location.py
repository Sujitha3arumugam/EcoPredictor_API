
from geopy.geocoders import Nominatim
import requests

def get_coordinates(location_name):
    geolocator = Nominatim(user_agent="eco_api")
    location = geolocator.geocode(location_name)
    if not location:
        raise Exception("Location not found")
    return location.latitude, location.longitude, location.address

def get_current_ip_location():
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()
        city = data.get("city")
        if not city:
            raise Exception("City not found in IP location data")
        return city
    except Exception as e:
        raise Exception(f"Failed to fetch IP-based location: {str(e)}")
