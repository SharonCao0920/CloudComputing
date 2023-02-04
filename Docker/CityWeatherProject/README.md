# **City - Weather Project**
### *This project is to convert City name to Weather information with 2 Microservices using docker containers/images*
<img width="218" alt="requirement" src="https://user-images.githubusercontent.com/54694766/216755576-b92fc68a-2849-40db-a170-c0c8a2df7a50.png">

### File Structure
<img width="170" alt="Screenshot_20230203_083248" src="https://user-images.githubusercontent.com/54694766/216756107-622d20f7-639b-4096-aebf-d2f49df2caf9.png">

## **Create Two Microservices**

* **Microservice 1:** Convert City Name to Zipcode

<img width="372" alt="m1" src="https://user-images.githubusercontent.com/54694766/216755588-9d82b458-12d0-468b-b0e7-ece739ea207c.png">

[**image build and container run details**](https://github.com/SharonCao0920/CloudComputing/tree/main/Docker/CityWeatherProject/CityWeather)

* **Microservice 2:** Convert Zipcode to Weather information

<img width="230" alt="m2" src="https://user-images.githubusercontent.com/54694766/216755599-a20cf1dc-783d-4854-accb-2307a9c7b685.png">

[**image build and container run details**](https://github.com/SharonCao0920/CloudComputing/tree/main/Docker/CityWeatherProject/ZipWeather)

## **Step 1: Docker Desktop Images and Containers**
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


