#FROM python:3.8.8-slim 
FROM python:3.9-slim
RUN  apt-get update && apt-get -y install cron vim

RUN pip3 install --upgrade pip

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

COPY . .
EXPOSE 6071

CMD ["python", "app/main.py"]