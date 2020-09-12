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
import requests
import time
from requests.exceptions import HTTPError
from weather import Weather


class WeatherAPI:

    def __init__(self, api_code, lang, base_url, reconTime):

        # mögliche Eingabefehler abfangen
        if api_code == None:
            raise Exception(
                "Missing parameter 'api_code' in the WeatherAPI-Constructor. No value given.")
        if lang == None:
            raise Exception(
                "Missing parameter 'lang' in the WeatherAPI-Constructor. No value given.")
        elif base_url == None:
            raise Exception(
                "Missing parameter 'base_url' in the WeatherAPI-Constructor. No value given.")
        elif reconTime == None:
            raise Exception(
                "Missing parameter 'reconTime' in the WeatherAPI-Constructor. No value given.")
        elif type(api_code) == int or type(api_code) == float:
            raise Exception(
                "Wrong parameter type for 'api_code' in the WeatherAPI-Constructor.")
        elif type(lang) == int or type(lang) == float:
            raise Exception(
                "Wrong parameter type for 'lang' in the WeatherAPI-Constructor.")
        elif type(base_url) == int or type(base_url) == float:
            raise Exception(
                "Wrong parameter type for 'base_url' in the WeatherAPI-Constructor.")
        elif type(reconTime) != int:
            raise Exception(
                "Wrong parameter type for 'reconTime' in the WeatherAPI-Constructor.")
        elif len(api_code) == 0:
            raise Exception(
                "Wrong value for 'api_code' in the WeatherAPI-Constructor.")
        elif len(lang) == 0:
            raise Exception(
                "Wrong value for 'lang' in the WeatherAPI-Constructor.")
        elif len(base_url) == 0:
            raise Exception(
                "Wrong value for 'base_url' in the WeatherAPI-Constructor.")
        elif reconTime < 1:
            raise Exception(
                "Inconsistent value for 'reconTime' in the WeatherAPI-Constructor. Value have to be geater then 0.")

        self.__api_code = api_code
        self.__lang = lang
        self.__base_url = base_url
        self.__reconTime = reconTime

    """
    Generate request url for openweathermap
    """

    def __generateURL(self, location):
        return "{0}q={1}&appid={2}&lang={3}".format(self.__base_url, location, self.__api_code, self.__lang)

    """
    Convert http response to json string
    """

    def __parseData(self, response, tstamp):

        json_data = response.json()

        weather_obj = Weather(tstamp=tstamp)
        # weather_obj.set_tstamp(tstamp)

        if 'name' in json_data:
            weather_obj.set_station_name(json_data['name'])

        if 'country' in json_data['sys']:
            weather_obj.set_country(json_data['sys']['country'])

        """
        manage tempeature informations
        """
        if 'temp' in json_data['main']:
            weather_obj.set_temp(
                round(float(json_data['main']['temp'] - 273), 2))

        if 'feels_like' in json_data['main']:
            weather_obj.set_feels_like(round(
                float(json_data['main']['feels_like'] - 273), 2))

        if 'pressure' in json_data['main']:
            weather_obj.set_pressure(
                round(float(json_data['main']['pressure']), 2))

        if 'humidity' in json_data['main']:
            weather_obj.set_humidity(
                round(float(json_data['main']['humidity']), 2))

        if 'temp_max' in json_data['main']:
            weather_obj.set_temp_max(
                round(float(json_data['main']['temp_max']-273), 2))

        if 'temp_min' in json_data['main']:
            weather_obj.set_temp_min(
                round(float(json_data['main']['temp_min']-273), 2))

        """
        manage wind informations
        """
        if 'speed' in json_data['wind']:
            weather_obj.set_wind_speed(
                round(float(json_data['wind']['speed']), 2))

        if 'deg' in json_data['wind']:
            weather_obj.set_wind_deg(round(float(json_data['wind']['deg']), 2))

        """
        manage cloud informations
        """
        if 'clouds' in json_data:
            if 'all' in json_data['clouds']:
                weather_obj.set_clouds_all(int(json_data['clouds']['all']))

        """
        manage rain informations
        """
        if 'rain' in json_data:
            if '1h' in json_data['rain']:
                weather_obj.set_rain1h(
                    round(float(json_data['rain']['1h']), 2))

            if '3h' in json_data['rain']:
                weather_obj.set_rain3h(
                    round(float(json_data['rain']['3h']), 2))

        """
        manage snow informations
        """
        if 'snow' in json_data:
            if '1h' in json_data['rain']:
                weather_obj.set_snow1h(
                    round(float(json_data['snow']['1h']), 2))

            if '3h' in json_data['rain']:
                weather_obj.set_snow3h(
                    round(float(json_data['snow']['3h']), 2))

        """
        manage view informations
        """
        if 'visibility' in json_data:
            weather_obj.set_visibility(int(json_data['visibility']))

        """
        system values
        """
        if 'sunrise' in json_data['sys']:
            weather_obj.set_sunrise(int(json_data['sys']['sunrise']))

        if 'sunset' in json_data['sys']:
            weather_obj.set_sunset(int(json_data['sys']['sunset']))

        for item in json_data['weather']:
            weather_obj.set_main(item['main'])
            weather_obj.set_description(item['description'])

        return weather_obj

    """
    Read weather informations at specific location
    """

    def fetchWeatherData(self, location):
        url = self.__generateURL(location)

        cnct_verusche = 0  # Anzahl der Verbindungsversuche
        status = 0

        while (cnct_verusche < 3):
            response = requests.get(url)
            status = response.status_code
            cnct_verusche += 1

            if status == 200:
                break
            else:
                print(
                    "> Request failed. Try {0}/3".format(cnct_verusche))

                t0 = time.time()
                while(time.time() < t0+self.__reconTime):
                    pass

        if status == 200:
            tstamp = time.time()
            return self.__parseData(response, tstamp)
        else:
            raise Exception(
                "No connection with API Server possible.")

    """
    Print weather informations on screen
    """

    def printWeatherData(self, weather_data):

        # Calculate time for timestamp, sunrise and sunset
        t_rise = time.localtime(weather_data.get_sunrise())
        t_set = time.localtime(weather_data.get_sunset())
        t_stamp = time.localtime(weather_data.get_tstamp())

        print("Received following weather informations for the location {0} [{1}]:".format(
            weather_data.get_station_name(), weather_data.get_country()))
        print("Temperature: {0} °C".format(weather_data.get_temp()))
        print("Fells like: {0}".format(weather_data.get_feels_like()))
        print("Temp. max: {0} °C".format(weather_data.get_temp_max()))
        print("Temp. min: {0} °C".format(weather_data.get_temp_min()))
        print("Humidity: {0} %".format(
            weather_data.get_humidity()))

        print("Air pressure: {0} hPa".format(weather_data.get_pressure()))
        print("Cloud density: {0}".format(weather_data.get_clouds_all()))
        print("View: {0}".format(weather_data.get_visibility()))
        print(
            "Wind speed: {0} m/s".format(weather_data.get_wind_speed()))
        print("Wind direction: {0} Deg.".format(weather_data.get_wind_deg()))
        print("Rain (1h): {0}".format(weather_data.get_rain1h()))
        print("Rain (3h): {0}".format(weather_data.get_rain3h()))
        print("Snow (1h): {0}".format(weather_data.get_snow1h()))
        print("Snow (3h): {0}".format(weather_data.get_snow3h()))
        print("Description: {0}".format(weather_data.get_description()))
        print("Main: {0}".format(weather_data.get_main()))
        print("Sunrise: {0}:{1}:{2}".format(
            t_rise.tm_hour, t_rise.tm_min, t_rise.tm_sec))
        print("Sunset: {0}:{1}:{2}".format(
            t_set.tm_hour, t_set.tm_min, t_set.tm_sec))
        print("requested at: {0}.{1}.{2} - {3}:{4}:{5}".format(t_stamp.tm_mday,
                                                               t_stamp.tm_mon, t_stamp.tm_year, t_stamp.tm_hour, t_stamp.tm_min, t_stamp.tm_sec))
