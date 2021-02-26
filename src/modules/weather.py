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

import time


class Weather:

    def __init__(self, data=None):
        self.__columns = {
            "temp": {
                "datatype": "float",
                "jsonName": "main.temp",
                "name": "Temperature",
                "value": None
            },
            "temp_min": {
                "datatype": "float",
                "jsonName": "main.temp_min",
                "name": "Temperature min.",
                "value": None
            },
            "temp_max": {
                "datatype": "float",
                "jsonName": "main.temp_max",
                "name": "Temperature max.",
                "value": None
            },
            "feels_like": {
                "datatype": "float",
                "jsonName": "main.feels_like",
                "name": "Temperature feels like",
                "value": None
            },
            "pressure": {
                "datatype": "int",
                "jsonName": "main.pressure",
                "name": "Pressure",
                "value": None
            },
            "humidity": {
                "datatype": "int",
                "jsonName": "main.humidity",
                "name": "Humidity",
                "value": None
            },
            "visibility": {
                "datatype": "int",
                "jsonName": "visibility",
                "name": "Visibility",
                "value": None
            },
            "wind_speed": {
                "datatype": "float",
                "jsonName": "wind.speed",
                "name": "Wind speed",
                "value": None
            },
            "wind_deg": {
                "datatype": "int",
                "jsonName": "wind.deg",
                "name": "Wind direction",
                "value": None
            },
            "clouds": {
                "datatype": "int",
                "jsonName": "clouds.all",
                "name": "Clouds index",
                "value": None
            },
            "description": {
                "datatype": "string",
                "jsonName": "weather.description",
                "name": "Description",
                "value": None
            },
            "rain1h": {
                "datatype": "float",
                "jsonName": "rain.rain1h",
                "name": "Rain 1h",
                "value": None
            },
            "rain3h": {
                "datatype": "float",
                "jsonName": "rain.rain3h",
                "name": "Rain 3h",
                "value": None
            },
            "snow1h": {
                "datatype": "float",
                "jsonName": "snow.snow1h",
                "name": "Snow 1h",
                "value": None
            },
            "snow3h": {
                "datatype": "float",
                "jsonName": "snow.snow3h",
                "name": "Snow 1h",
                "value": None
            },
            "sunrise": {
                "datatype": "timestamp",
                "jsonName": "sys.sunrise",
                "name": "Sunrise",
                "value": None
            },
            "sunset": {
                "datatype": "timestamp",
                "jsonName": "sys.sunset",
                "name": "Sunset",
                "value": None
            },
            "tstamp": {
                "datatype": "timestamp",
                "jsonName": "tstamp",
                "name": "Timestamp",
                "value": None
            }
        }
        # end of self.__columns

        """
        convert list to column data
        """
        # check if valid datatype
        if data == None:
            return
        elif type(data) != dict:
            raise Exception(
                "Invalid type for data. dict was expected to initialize weather object.")

        self.__convertDictToDataColumns(data)

    def __convertDictToDataColumns(self, data):
        # loop all column entries
        for col in self.__columns:
            # extract json name from column entry
            jsonNameList = self.__columns[col]["jsonName"].split(".")
            itemData = data.get(jsonNameList[0])
            if type(itemData) == dict:
                itemData = itemData.get(jsonNameList[1])
            elif type(itemData) == list:
                itemData = itemData[0].get(jsonNameList[1])
            elif type(itemData) == float or type(itemData) == int:
                pass
            else:
                continue

            # check if datatype is valid for specific column
            if self.__checkDatatype(itemData, col):
                self.__columns[col]["value"] = itemData

    def __checkDatatype(self, value, columnName):
        dtype = self.__columns[columnName]["datatype"]
        if dtype == "string" and type(value) != str:
            raise Exception(
                "Wrong format for column data '{0}'. Type string was expected.".format(columnName))
        elif dtype == "int" and type(value) != int:
            raise Exception(
                "Wrong format for column data '{0}'. Type int was expected.".format(columnName))
        elif dtype == "float" and type(value) != float:
            raise Exception(
                "Wrong format for column data '{0}'. Type float was expected.".format(columnName))
        elif dtype == "timestamp" and not (type(value) == int or type(value) == float):
            raise Exception(
                "Wrong format for column data '{0}'. Type float or int was expected.".format(columnName))

        return True

    def setItem(self, columnName, value):
        if self.__columns.get(columnName) == None:
            raise Exception(
                "Column name '{0}' is not available".format(columnName))
        elif(self.__checkDatatype(value, columnName)):
            self.__columns.get(columnName)["value"] = value

    def getItem(self, columnName):
        ret = self.__columns.get(columnName)
        if ret == None:
            raise Exception(
                "Column name '{0}' is not available.".format(columnName))
        elif self.__columns.get(columnName).get("datatype") == "timestamp":
            t = time.localtime(ret.get("value"))
            return "{0}.{1}.{2} {3}:{4}:{5}".format(t.tm_mday, t.tm_mon, t.tm_year, t.tm_hour, t.tm_min, t.tm_sec)
        return ret.get("value")
