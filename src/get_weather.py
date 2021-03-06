'''
This file is part of OpenWeather-Datalogger

Copyright (C) 2021  Jean-Marcel Herzog

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

# -*- coding: utf-8 -*-

from modules.weatherapi import WeatherAPI
from modules.mongodriver import MongoDriver
from modules.weather import Weather

"""
Globale Parameter
"""
# API parameters
api_code = ''  # your API key
lang = 'de'
weather_locations = []
base_url = 'http://api.openweathermap.org/data/2.5/weather?'
req_recon_time = 10  # seconds

# database parameters
db_host = "127.0.0.1"
db_port = "27017"
db_user = '#'
db_pass = '#'

try:

    """
    initialize API and database
    """
    api = WeatherAPI(api_code, lang, base_url, req_recon_time)
    mongo = MongoDriver(db_host, db_port, db_user, db_pass)

    """
	get weather data
	"""
    for location in weather_locations:
        weather_data = api.fetchWeatherData(location)

        if weather_data != None:
            # api.printWeatherData(weather_data)
            mongo.insertEntry(location, weather_data.toJSON())

except ValueError as verr:
    print("[WARNING] {0}".format(verr))
except Exception as err:
    print("[ERROR] {0}".format(err))
