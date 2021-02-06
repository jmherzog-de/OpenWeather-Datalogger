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

import json
import time
import pymongo

from modules.weather import Weather


class MongoDriver:

    """
    Constructor
    """

    def __init__(self, host, port, username, password):
        self.__host = host
        self.__port = port
        self.__client = pymongo.MongoClient(
            "mongodb://{2}:{3}@{0}:{1}/".format(host, port, username, password))

    """
    write weather data informations into database
    """

    def insertEntry(self, collection_name, data):
        database = self.__client["weathercrawler"]
        data.pop("station_name")
        data.pop("country")
        collection = database[str(collection_name)]
        return collection.insert_one(data)

    """
    return all weather data entries from database
    """

    def getAll(self, collection_name):
        database = self.__client["weathercrawler"]
        collection = database[str(collection_name)]
        return collection.find()

    """
    return last entry of collection
    """
    def getLastEntry(self, collection_name):
        database = self.__client["weathercrawler"]
        collection = database[str(collection_name)]
        lastEntry = collection.find_one(sort=[('$natural',-1)])

        #return lastEntry
        #lastEntry = collection.find().sort([('$natural',-1)]).limit(1)
        weatherObj = Weather()
        weatherObj.set_tstamp(lastEntry['tstamp'])
        weatherObj.set_temp(lastEntry['temp'])
        weatherObj.set_temp_max(lastEntry['temp_max'])
        weatherObj.set_temp_min(lastEntry['temp_min'])
        weatherObj.set_feels_like(lastEntry['feels_like'])
        weatherObj.set_description(lastEntry['description'])
        weatherObj.set_pressure(lastEntry['pressure'])
        weatherObj.set_humidity(lastEntry['humidity'])
        weatherObj.set_wind_speed(lastEntry['wind_speed'])
        weatherObj.set_wind_speed(lastEntry['wind_deg'])
        
        if lastEntry['wind_deg'] != None:
            weatherObj.set_wind_deg(float(lastEntry['wind_deg']))
        weatherObj.set_clouds_all(lastEntry['clouds_all'])
        if lastEntry['rain1h'] != None:
            weatherObj.set_rain1h(lastEntry['rain1h'])
        if lastEntry['rain3h'] != None:
            weatherObj.set_rain3h(lastEntry['rain3h'])
        if lastEntry['snow1h'] != None:
            weatherObj.set_snow1h(lastEntry['snow1h'])
        if lastEntry['snow3h'] != None:
            weatherObj.set_snow3h(lastEntry['snow3h'])
        if lastEntry['visibility'] != None:
            weatherObj.set_visibility(lastEntry['visibility'])
        weatherObj.set_sunrise(lastEntry['sunrise'])
        weatherObj.set_sunset(lastEntry['sunset'])
        weatherObj.set_main(lastEntry['main'])
        weatherObj.set_description(lastEntry['description'])
        weatherObj.set_tstamp(lastEntry['tstamp'])
        
        return weatherObj