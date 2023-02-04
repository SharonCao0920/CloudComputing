
from flask import Flask, request

app = Flask(__name__)

# Hardcoded zip code to weather mapping
weather_data = {
    "10001": "Sunny",
    "90001": "Rainy",
    "60601": "Cloudy",
    "95035": "Sunny"
}

@app.route("/weather")
def get_weather():
    zip_code = request.args.get("zip_code")
    weather = weather_data.get(zip_code, "Not available")
    return f"<h3>Zip code: {zip_code}</h3><br><h3>Weather: {weather}</h3>"

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5001, debug = True)
