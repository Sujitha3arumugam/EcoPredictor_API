
from fastapi import FastAPI, Query
from .location import get_coordinates, get_current_ip_location
from .weather import get_temperature
from .predictor import calculate_tree_need, suggest_plants

app = FastAPI()

@app.get("/predict")
def predict(location: str = Query(..., description="City or address")):
    lat, lon, loc_name = get_coordinates(location)
    temperature = get_temperature(lat, lon)
    trees_needed = calculate_tree_need(temperature)
    recommendations = suggest_plants(trees_needed)
    return {
        "location": loc_name,
        "temperature": f"{temperature} °C",
        "trees_needed": trees_needed,
        "recommendations": recommendations
    }

@app.get("/predict/current")
def predict_current_location():
    current_city = get_current_ip_location()
    lat, lon, loc_name = get_coordinates(current_city)
    temperature = get_temperature(lat, lon)
    trees_needed = calculate_tree_need(temperature)
    recommendations = suggest_plants(trees_needed)
    return {
        "location": loc_name,
        "temperature": f"{temperature} °C",
        "trees_needed": trees_needed,
        "recommendations": recommendations
    }
