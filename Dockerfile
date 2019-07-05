FROM python:3.6-alpine
WORKDIR /app
COPY . /app
VOLUME /app/logg
CMD ["python", "./dlogt.py"]
