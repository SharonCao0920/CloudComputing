# **City - Weather Project**
*This project is to convert City name search to Weather information with Microservices*

![My Image](./image/requirement.png)

## **Create Two Microservices**

* **Microservice 1:** Convert City Name to Zipcode

![My Image](./image/m1.png)

[**Details**](https://github.com/SharonCao0920/CloudComputing/tree/main/Docker/CityWeatherProject/CityZipcode)

* **Microservice 2:** Convert Zipcode to Weather information

![My Image](./image/m2.png)

[**Details**](https://github.com/SharonCao0920/CloudComputing/tree/main/Docker/CityWeatherProject/ZipWeather)

## **Docker Desktop Images and Containers**
![My Image](./image/images.png)
![My Image](./image/containers.png)


## **Push Images to DockerHub**
Check Images Created
```
$ docker images
```
![My Image](./image/localimage.png)

Create tags for Images
```
$ docker tag 752034694e8f sharoncao0920/citytoweather:cityserver 
$ docker tag c5651927e444 sharoncao0920/citytoweather:zipweather
```
![My Image](./image/createtags.png)

Push Image Tags to DockerHub
```
$ docker push sharoncao0920/citytoweather:cityserver
```
![My Image](./image/pushimage.png)

```
$ docker push sharoncao0920/citytoweather:zipweather
```
![My Image](./image/pushimage1.png)

Check Result on DockerHub

![My Image](./image/dockeruhb.png)
