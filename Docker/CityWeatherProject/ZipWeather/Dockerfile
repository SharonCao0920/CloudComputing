FROM python:3.11-alpine

RUN apk add --no-cache build-base

COPY . /app

WORKDIR /app

EXPOSE 8888

CMD ["python", "zipserver.py"]

