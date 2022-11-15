FROM python:3.8-slim-buster

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

RUN apt-get update -y

RUN apt-get install -y libgomp1

ENTRYPOINT [ "streamlit", "run", "app.py", "--server.port=8080", "server.address=0.0.0.0" ]