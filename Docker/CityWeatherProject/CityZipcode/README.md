# **Microservice 1: City Name to Zipcode**

## **Setp 1: Create cityweather.py**
*Requirement: Take in city name and use the city zipcode to call service 2 to get weather information on browser*

```
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
```

## **Step 2: Create Dockerfile**
```
# Dockerfile for zip code to weather server
FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install Flask
RUN pip install requests
EXPOSE 5000
CMD ["python", "cityweather.py"]
```

## **Step 3: Build Image**
### **Build Image**
```
$ docker build -t city-weather .
```
<img width="1437" alt="Screenshot_20230203_111926" src="https://user-images.githubusercontent.com/54694766/216754667-d8b67e50-505b-4d0b-ac80-3355987511f3.png">

### **Check on Docker**
<img width="739" alt="Screenshot_20230203_112134" src="https://user-images.githubusercontent.com/54694766/216754722-aadb8441-8659-4ead-8eb1-45a80391d446.png">

## **Step 4: Start a Container from this Image**

### **Run Container**
```
$ docker run --name city-weather-container -p 5000:5000 city-weather
```
<img width="1464" alt="Screenshot_20230203_112238" src="https://user-images.githubusercontent.com/54694766/216754771-7a6769be-675c-4650-904c-0c8ddb4059e6.png">

### **Check on Docker**
<img width="739" alt="Screenshot_20230203_112309" src="https://user-images.githubusercontent.com/54694766/216754783-fa9db4b7-cf84-417a-97bf-5f65ec299214.png">

