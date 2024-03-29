# **Microservice 2: Zipcode to Weather**

## **Setp 1: Create zipweather.py**
### *Requirement: Convert zipcode to weather information*

```
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

```

## **Step 2: Create Dockerfile**
```
# Dockerfile for city to zip code server
FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install Flask
EXPOSE 8000
CMD ["python", "zipweather.py"]
```

## **Step 3: Build Image**
### **Build Image**
```
$ docker build -t zip-weather .
```
<img width="1464" alt="Screenshot_20230203_113626" src="https://user-images.githubusercontent.com/54694766/216755295-dd57e890-3512-41e3-9d80-7bd70ef3058e.png">


### **Check on Docker**
<img width="741" alt="Screenshot_20230203_113712" src="https://user-images.githubusercontent.com/54694766/216755332-31ef8025-4d40-480e-a960-d11fa06d339d.png">

## **Step 4: Start a Container from this Image**

### **Run Container**
```
$ docker run --name zip-weather-container -p 5001:5001 zip-weather
```
<img width="1447" alt="Screenshot_20230203_113747" src="https://user-images.githubusercontent.com/54694766/216755383-1097ff1c-9ff5-4171-9866-73ab7026c618.png">

### **Check on Docker**
<img width="753" alt="Screenshot_20230203_113854" src="https://user-images.githubusercontent.com/54694766/216755396-9ded8448-dc59-4224-a903-4376b14ecd70.png">

## **Step 5: Push Images to DockerHub**

**Create Tags for Images**
```
$ docker tag city-weather sharoncao0920/citytoweather:cityweather
```
<img width="914" alt="Screenshot_20230204_124706" src="https://user-images.githubusercontent.com/54694766/216758102-62c9551a-3046-4ae9-923f-f41b9f85013d.png">


**Push Image Tags to DockerHub**
```
$ docker push sharoncao0920/citytoweather:cityweather
```
<img width="935" alt="Screenshot_20230204_124801" src="https://user-images.githubusercontent.com/54694766/216758144-4f6c36d5-7c49-4182-aad6-1f85eac57aa6.png">

**Check Result on DockerHub**
<img width="1031" alt="Screenshot_20230204_124847" src="https://user-images.githubusercontent.com/54694766/216758184-b054122e-2537-42c8-a7ef-9ac084a872d3.png">

