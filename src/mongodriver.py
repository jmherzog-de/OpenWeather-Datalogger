'''
This file is part of OpenWeather-Datalogger

Copyright (C) 2020  Jean-Marcel Herzog

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


class MongoDriver:

    """
    Constructor
    """

    def __init__(self, host, port):
        self.__host = host
        self.__port = port
        self.__client = pymongo.MongoClient(
            "mongodb://{0}:{1}/".format(host, port))

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
