# OpenWeather Datalogger

Fully Python written datalogger fetching weather informations from Openweathermap.org and store them at a mongodb database. This project provides a docker compse file to generate a container for maximum portability. This project was tested on RaspberryPi 3. API Requests for multiple locations included.

## Openweathermap.org API

The openweathermap organisation provide there API for free with the restriction of 1000 requests per day with a limit of 60 calls per hour. Other plans are available. There are no limitations for generating individuakl API keys.

Further informations:
[1] https://openweathermap.org/current

## Docker Container

docker-compose will generate two containers. A container including the mongodb database and another will provide the python3 environment to fetch weather informations. The container can be generated with the _docker-compose_ command.

```
docker-compose build
```

After the container have been built. You can start them with the following command:

```
docker-compose up -d
```

### Database

The database container is based on a compatible ARM image for mongodb V2. Access cover the port 21017. No further user credentials needed.

### Python3 Container

This container is based on a Ubuntu image and provides a Python3 environment. Furthermore some python libraries will be installed like pymongo and requests.
Note: Maybe the timezone of the container have to be changed. Sometimes wrong timestamps will be generated.

#### Python3 Container - Change timezone

After the container is up and running, the timezone must be changed for some users. Therefore the paket **tzdata** is needed. The required time zone is also set during installation process.

```
apt install tzdata
```

## Fetch weather informations

The weather from openweathermap can be fetched and saved with the python script _get_weather.py_. It is helpful to create a cronjob for this action.

### Create Cronjob

A corresponding cron job can be set up so that the weather informations can be fetched automatically. The following command must be entered in the terminal:

```
crontab -e
```

In the example below, the weather data is retrieved every 30 minutes:

```
LANG=de_DE.UTF-8
LANGUAGE=de
LC_TYPE=de_DE.UTF-8
PYTHONENCODING=utf8

*/30 * * * * python3 /home/src/get_weather.py >> /home/sc/logfile 2&>1
```

All screen outputs of the programm are saved in the log file located at _/home/src/logfile_.

Finally the crontab service has to be started.

```
service cron start
```

## Data monitoring with flask web application

The fetched data can be monitored with a python flask web application. Change debug option in file web_backend.py to False in
production mode.
