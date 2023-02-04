# Dockerfile for city to zip code server
FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install Flask
EXPOSE 8000
CMD ["python", "zipweather.py"]
