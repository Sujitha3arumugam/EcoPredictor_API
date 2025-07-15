
import requests
from .config import API_KEY

def get_temperature(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['main']['temp']
    raise Exception("Failed to fetch temperature")
