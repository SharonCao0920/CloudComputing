# **City - Weather Project**
### *This project is to convert City name to Weather information with 2 Microservices using docker containers/images*
<img width="218" alt="requirement" src="https://user-images.githubusercontent.com/54694766/216755576-b92fc68a-2849-40db-a170-c0c8a2df7a50.png">

### File Structure
<img width="170" alt="Screenshot_20230203_083248" src="https://user-images.githubusercontent.com/54694766/216756107-622d20f7-639b-4096-aebf-d2f49df2caf9.png">

## **Step 1: Create Two Microservices**

* **Microservice 1:** Convert City Name to Zipcode and call service 2 to get weather information

<img width="372" alt="m1" src="https://user-images.githubusercontent.com/54694766/216755588-9d82b458-12d0-468b-b0e7-ece739ea207c.png">

[**image build and container run details**](https://github.com/SharonCao0920/CloudComputing/tree/main/Docker/CityWeatherProject/CityWeather)

* **Microservice 2:** Convert Zipcode to Weather information

<img width="230" alt="m2" src="https://user-images.githubusercontent.com/54694766/216755599-a20cf1dc-783d-4854-accb-2307a9c7b685.png">

[**image build and container run details**](https://github.com/SharonCao0920/CloudComputing/tree/main/Docker/CityWeatherProject/ZipWeather)

### Images
<img width="942" alt="Screenshot_20230203_114622" src="https://user-images.githubusercontent.com/54694766/216755673-3000c4e8-fbc3-4673-a7ba-bde18e87160f.png">

**Check Images Created**
```
$ docker images
```
<img width="728" alt="Screenshot_20230203_114809" src="https://user-images.githubusercontent.com/54694766/216755756-733f940b-0c09-4bd3-9e89-d2ebdb70a890.png">

### Containers
<img width="946" alt="Screenshot_20230203_114732" src="https://user-images.githubusercontent.com/54694766/216755709-ee4ee5e0-a0b3-4843-9443-5d42ba26b123.png">

**Check Containers Running**
```
$ docker ps
or
$ docker container ls
```
<img width="1463" alt="Screenshot_20230203_114855" src="https://user-images.githubusercontent.com/54694766/216755808-ec030d72-43aa-4736-b3b9-554b58fd47d7.png">

**DockerHub**
<img width="999" alt="Screenshot_20230204_125018" src="https://user-images.githubusercontent.com/54694766/216758249-b66273a3-61d6-4a8e-821f-93cb27f1e481.png">


## **Step 2: Set Up Docker Network**

### Create Docker Network
```
$ docker network create city-weather-network
```

### Check Available Network
```
$ docker network ls
```
<img width="721" alt="Screenshot_20230204_121020" src="https://user-images.githubusercontent.com/54694766/216756583-c483b91d-d736-48f9-a6e8-bb962633fe00.png">

### Inspect Network Before Adding Containers
```
$ docker network inspect city-weather-network
```
<img width="947" alt="Screenshot_20230204_121228" src="https://user-images.githubusercontent.com/54694766/216756700-4c62e3ee-97d0-456e-ad8a-5fe917c7b30e.png">


### Add Containers to Network
```
$ docker network connect city-weather-network city-weather-container
$ docker network connect city-weather-network zip-weather-container
```

### Inspect Network Again to Make Sure Containers Added
<img width="1027" alt="Screenshot_20230204_121538" src="https://user-images.githubusercontent.com/54694766/216756789-cb96b229-1a2c-431c-af91-241097f74e4c.png">

## **Step 3: Verify Communication Between Containers**

### On Browser

**Go to http://127.0.0.1:5000**

<img width="484" alt="Screenshot_20230204_122019" src="https://user-images.githubusercontent.com/54694766/216756974-869a23d9-909f-4e38-8190-5b57cdc82bcd.png">

**Go to http://127.0.0.1:5000/cityweather** (No City Information)

<img width="519" alt="Screenshot_20230204_123256" src="https://user-images.githubusercontent.com/54694766/216757528-ede1e05c-e44a-4c5a-8403-b52659e6b017.png">

**Go to http://127.0.0.1:5000/cityweather?city={city}**

<img width="713" alt="Screenshot_20230204_123133" src="https://user-images.githubusercontent.com/54694766/216757491-a0db9821-e0f8-43b3-adfa-a5966db906bb.png">
<img width="686" alt="Screenshot_20230204_123215" src="https://user-images.githubusercontent.com/54694766/216757508-f2040fb0-d901-4e54-8776-7e069efcc999.png">

**Container2: http://127.0.0.1:5001/weather?zip_code={zip_code}**

<img width="439" alt="Screenshot_20230204_123559" src="https://user-images.githubusercontent.com/54694766/216757644-08f197bc-3620-4053-941b-6fa380a25cdb.png">


### With curl
**In terminal**
```
culr http://127.0.0.1:5000/
```
<img width="1207" alt="Screenshot_20230204_122444" src="https://user-images.githubusercontent.com/54694766/216757185-87acad4d-da0c-4df3-bd3d-391404143c7e.png">

```
culr http://127.0.0.1:5000/cityweather
```
<img width="1209" alt="Screenshot_20230204_122642" src="https://user-images.githubusercontent.com/54694766/216757278-9fe132de-c92d-4db8-afbf-f82090d84df1.png">

```
culr http://127.0.0.1:5000/cityweather?city=Milpitas
```
<img width="1222" alt="Screenshot_20230204_122747" src="https://user-images.githubusercontent.com/54694766/216757325-3b1b0e08-daca-4e6e-8e63-f6844938bfa6.png">

```
curl http://127.0.0.1:5001/weather?zip_code=10001
```
<img width="1202" alt="Screenshot_20230204_123704" src="https://user-images.githubusercontent.com/54694766/216757695-189e68e4-2448-433e-bec5-2b8bd97d199d.png">
