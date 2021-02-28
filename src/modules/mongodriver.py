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

    def __init__(self, host, port, database, username, password):
        self.__host = host
        self.__port = port
        self.__db = str(database)
        self.__client = pymongo.MongoClient(
            "mongodb://{2}:{3}@{0}:{1}/".format(host, port, username, password))

    """
    Return collection name for given location
    """

    def generateCollectionName(self, location):
        formattedLoc = location.lower().replace(" ", "_")
        formattedLoc = formattedLoc.replace("ä", "ae").replace("Ä", "ae")
        formattedLoc = formattedLoc.replace("ö", "oe").replace("Ö", "Oe")
        formattedLoc = formattedLoc.replace("ü", "ue").replace("Ü", "Ue")
        return formattedLoc.replace("ß", "ss")

    """
    write weather data informations into database
    """

    def insertEntry(self, collection_name, data):
        collection_name = self.generateCollectionName(collection_name)
        database = self.__client[self.__db]
        data.pop("station_name")
        data.pop("country")
        collection = database[str(collection_name)]
        return collection.insert_one(data)

    """
    write raw json response from api into database
    """

    def insertRawJSON(self, collection_name, jsonData):
        collection_name = self.generateCollectionName(collection_name)
        database = self.__client[self.__db]
        collection = database[str(collection_name)]
        return collection.insert_one(jsonData)

    """
    return all raw entries as list from database
    """

    def getAllRawAsList(self, collection_name):
        collection_name = self.generateCollectionName(collection_name)
        database = self.__client[self.__db]
        collection = database[str(collection_name)]
        return list(collection.find({}))

    """
    return all entries as Weather object list
    """

    def getAllAsList(self, collection_name):
        collection_name = self.generateCollectionName(collection_name)
        retList = []
        for item in self.getAllRawAsList(collection_name):
            retList.append(Weather(item))
        return retList

    """
    drop a specific collection from database
    """

    def dropCollection(self, collection_name):
        collection_name = self.generateCollectionName(collection_name)
        database = self.__client[self.__db]
        collection = database[str(collection_name)]
        collection.drop()

    """
    return a set of entries with sorted elements
    format = False return dict otherwise return list of Weather objects
    """

    def getRows(self, collection_name, limit=None, DESC=False, format=False):
        collection_name = self.generateCollectionName(collection_name)
        database = self.__client[self.__db]
        collection = database[str(collection_name)]
        ret = collection.find({})
        if DESC == True:
            ret.sort("tstamp", -1)
        if limit != None:
            ret.limit(limit)
        if format == False:
            return ret

        retList = []
        for item in ret:
            retList.append(Weather(item))
        return retList
