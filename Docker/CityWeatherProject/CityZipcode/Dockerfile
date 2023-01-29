FROM python:3.11-alpine

RUN apk add --no-cache build-base

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "citysever.py"]
