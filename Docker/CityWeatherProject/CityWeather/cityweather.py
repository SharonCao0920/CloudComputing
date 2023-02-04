import requests
from flask import Flask, request

app = Flask(__name__)

# Hardcoded city to zip code mapping
zip_code_data = {
    "New York": "10001",
    "Los Angeles": "90001",
    "Chicago": "60601",
    "Milpitas": "95035"
}
@app.route("/")
def ping_service():
    return "Hello, Welcome to weather service!"

@app.route("/cityweather")
def get_zipcode_and_weather():
    city = request.args.get("city")
    zip_code = zip_code_data.get(city, "Not available")
    if zip_code == "Not available":
        return f"<h1>City: {city}</h1><br><h3>Zip code: {zip_code}</h3><br><h3>Weather: Not available</h3>"
    
    weather = requests.get(f"http://zip-weather-container:5001/weather?zip_code={zip_code}").text
    return f"<h1>City: {city}</h1><br><h2>Weather:</h2><br><h3>{weather}</h3>"

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True)