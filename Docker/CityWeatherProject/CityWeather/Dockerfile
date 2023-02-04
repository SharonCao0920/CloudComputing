# Dockerfile for zip code to weather server
FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install Flask
RUN pip install requests
EXPOSE 5000
CMD ["python", "cityweather.py"]
