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

    def __init__(self, station_name=None, country=None, temp=None, temp_max=None, temp_min=None, feels_like=None, pressure=None, humidity=None, wind_speed=None, wind_deg=None, clouds_all=None, rain1h=None, rain3h=None, snow1h=None, snow3h=None, visibility=None, sunrise=None, sunset=None, main=None, description=None, tstamp=None):
        self.__station_name = station_name
        self.__country = country
        self.__temp = temp
        self.__temp_max = temp_max
        self.__temp_min = temp_min
        self.__feels_like = feels_like
        self.__pressure = pressure
        self.__humidity = humidity
        self.__wind_speed = wind_speed
        self.__wind_deg = wind_deg
        self.__clouds_all = clouds_all
        self.__rain1h = rain1h
        self.__rain3h = rain3h
        self.__snow1h = snow1h
        self.__snow3h = snow3h
        self.__visibility = visibility
        self.__sunrise = sunrise
        self.__sunset = sunset
        self.__main = main
        self.__description = description
        self.__tstamp = tstamp

    def set_station_name(self, station_name):
        if type(station_name) == int or type(station_name) == float:
            raise Exception(
                "Wrong format for the parameter 'station_name' in set_station_name(...). A string was expected.")
        self.__station_name = station_name

    def get_station_name(self):
        return self.__station_name

    def set_country(self, country):
        if type(country) == int or type(country) == float:
            raise Exception(
                "Wrong format for the parameter 'country' in set_country(...). A string was expected.")
        self.__country = country

    def get_country(self):
        return self.__country

    def set_temp(self, temp):
        if type(temp) != float:
            raise Exception(
                "Wrong format for the parameter 'temp' in set_temp(...). A float was expected.")
        elif temp >= 50.0 or temp <= -30.0:
            raise ValueError(
                "Inconsistent value for 'temp' in set_temp(...) detected.")
        self.__temp = temp

    def get_temp(self):
        return self.__temp

    def set_temp_max(self, temp_max):
        if type(temp_max) != float:
            raise Exception(
                "Wrong format for the parameter 'temp_max' in set_temp_max(...). A float was expected.")
        elif temp_max >= 50.0 or temp_max <= -30.0:
            raise ValueError(
                "Inconsistent value for 'temp_max' in set_temp_max(...) detected.")

        self.__temp_max = temp_max

    def get_temp_max(self):
        return self.__temp_max

    def set_temp_min(self, temp_min):
        if type(temp_min) != float:
            raise Exception(
                "Wrong format for the parameter 'temp_min' in set_temp_min(...). A float wwas expected.")
        elif temp_min >= 50.0 or temp_min <= -30.0:
            raise ValueError(
                "Inconsistent value for 'temp_min' in set_temp_min(...) detected.")

        self.__temp_min = temp_min

    def get_temp_min(self):
        return self.__temp_min

    def set_feels_like(self, feels_like):
        if type(feels_like) != float:
            raise Exception(
                "Wrong format for the parameter 'feels_like' in set_feels_like(...). A float was expected.")
        elif feels_like >= 50.0 or feels_like <= -30.0:
            raise ValueError(
                "Inconsisten value for 'feels_like' in set_feels_like(...) detected.")

        self.__feels_like = feels_like

    def get_feels_like(self):
        return self.__feels_like

    def set_pressure(self, pressure):
        if type(pressure) != float:
            raise Exception(
                "Wrong format for the parameter 'pressure' in set_pressure(...). A float was expected.")
        elif pressure < 0.0:
            raise ValueError(
                "Inconsitent value for 'pressure' in set_pressure(...) detected.")

        self.__pressure = pressure

    def get_pressure(self):
        return self.__pressure

    def set_humidity(self, humidity):
        if type(humidity) != float:
            raise Exception(
                "Wrong format for the parameter 'humidity' in set_humidity(...). A float was expected.")
        elif humidity < 0.0 or humidity > 100.0:
            raise ValueError(
                "Inconsistent value fot parameter 'humidity' in set_humidity(...) detected.")

        self.__humidity = humidity

    def get_humidity(self):
        return self.__humidity

    def set_wind_speed(self, wind_speed):
        if type(wind_speed) != float:
            raise Exception(
                "Wrong format for the parameter 'wind_speed' in set_wind_speed(...). A float was expected.")
        elif wind_speed < 0.0:
            raise ValueError(
                "Inconsistent value for the parameter 'wind_speed' in set_wind_speed(...) detected.")

        self.__wind_speed = wind_speed

    def get_wind_speed(self):
        return self.__wind_speed

    def set_wind_deg(self, wind_deg):
        if type(wind_deg) != float:
            raise Exception(
                "Wrong format for the parameter 'wind_deg' in set_wind_deg(...). A float was expected.")
        elif wind_deg < 0.0:
            raise ValueError(
                "Inconsistent value for the parameter 'wind_deg' in set_wind_deg(...) detected.")

        self.__wind_deg = wind_deg

    def get_wind_deg(self):
        return self.__wind_deg

    def set_clouds_all(self, clouds_all):
        if type(clouds_all) != int:
            raise Exception(
                "Wrong format for the parameter 'clouds_all' in set_clouds_all(...). A int was expected.")
        elif clouds_all < 0:
            raise ValueError(
                "Inconsistent value for the parameter 'clouds_all' in set_clouds_all(...) detected.")

        self.__clouds_all = clouds_all

    def get_clouds_all(self):
        return self.__clouds_all

    def set_rain1h(self, rain1h):
        if type(rain1h) != float:
            raise Exception(
                "Wrong format for the parameter 'rain1h' in set_rain1h(...). A float was expected.")
        elif rain1h < 0.0:
            raise ValueError(
                "Inconsistent value for the parameter 'rain1h' in set_rain1h(...) detected.")

        self.__rain1h = rain1h

    def get_rain1h(self):
        return self.__rain1h

    def set_rain3h(self, rain3h):
        if type(rain3h) != float:
            raise Exception(
                "Wrong format for the parameter 'rain3h' in set_rain3h(...). A float was expected.")
        elif rain3h < 0.0:
            raise ValueError(
                "Inconsistent value for the parameter 'rain3h' in set_rain3h(...) detected.")

        self.__rain3h = rain3h

    def get_rain3h(self):
        return self.__rain3h

    def set_snow1h(self, snow1h):
        if type(snow1h) != float:
            raise Exception(
                "Wrong format for the parameter 'snow1h' in set_snow1h(...). A float was expected.")
        elif snow1h < 0.0:
            raise ValueError(
                "Inconsistent value for the parameter 'snow1h' in set_snow1h(...) detected.")

        self.__snow1h = snow1h

    def get_snow1h(self):
        return self.__snow1h

    def set_snow3h(self, snow3h):
        if type(snow3h) != float:
            raise Exception(
                "Wrong format for the parameter 'snow3h' in set_snow3h(...). A float was expected.")
        elif snow3h < 0.0:
            raise ValueError(
                "Inconsistent value for the parameter 'snow3h' in set_snow3h(...) detected.")

        self.__snow3h = snow3h

    def get_snow3h(self):
        return self.__snow3h

    def set_visibility(self, visibility):
        if type(visibility) != int:
            raise Exception(
                "Wrong format for the parameter 'visibility' in set_visibility(...). A int was expected.")
        elif visibility < 0:
            raise ValueError(
                "Inconsistent value for the parameter 'visibility' in set_visibility(...) detected.")

        self.__visibility = visibility

    def get_visibility(self):
        return self.__visibility

    def set_sunset(self, sunset):
        if type(sunset) != int:
            raise Exception(
                "Wrong format for the parameter 'sunset' in set_sunset(...). A int was expected.")
        elif sunset < 0.0:
            raise ValueError(
                "Inconsistent value for the parameter 'sunset' in set_sunset(...) detected.")

        self.__sunset = sunset

    def get_sunset(self, formatted=False):
        if self.__sunset == None:
            return None

        if formatted == False:
            return self.__sunset
        else:
            t = time.localtime(self.__sunset)
            return "{0}.{1}.{2} {3}:{4}:{5}".format(t.tm_mday, t.tm_mon, t.tm_year, t.tm_hour, t.tm_min, t.tm_sec)

    def set_sunrise(self, sunrise):
        if type(sunrise) != int:
            raise Exception(
                "Wrong format for the parameter 'sunrise' in set_sunrise(...). A int was expected.")
        elif sunrise < 0.0:
            raise ValueError(
                "Inconsistent value for the parameter 'sunrise' in set_sunrise(...) detected.")

        self.__sunrise = sunrise

    def get_sunrise(self, formatted=False):
        if self.__sunrise == None:
            return None

        if formatted == False:
            return self.__sunrise
        else:
            t = time.localtime(self.__sunrise)
            return "{0}.{1}.{2} {3}:{4}:{5}".format(t.tm_mday, t.tm_mon, t.tm_year, t.tm_hour, t.tm_min, t.tm_sec)

    def set_main(self, main):
        if type(main) == int or type(main) == float:
            raise Exception(
                "Wrong format for the parameter 'main' in set_main(...). A string was expected.")

        self.__main = main

    def get_main(self):
        return self.__main

    def set_description(self, description):
        if type(description) == int or type(description) == float:
            raise Exception(
                "Wrong format for the parameter 'description' in set_description(...). A string was expected.")

        self.__description = description

    def get_description(self):
        return self.__description

    def set_tstamp(self, tstamp):
        if type(tstamp) != float:
            raise Exception(
                "Wrong format for the parameter 'tstamp' in set_tstamp(...). A float was expected.")
        if tstamp < 0.0:
            raise ValueError(
                "Inconsistent value for the parameter 'tstamp' in set_tstamp(...) detected.")

        self.__tstamp = tstamp

    def get_tstamp(self, formatted=False):
        if self.__tstamp == None:
            return None

        if formatted == False:
            return self.__tstamp
        else:
            t = time.localtime(self.__tstamp)
            return "{0}.{1}.{2} {3}:{4}:{5}".format(t.tm_mday, t.tm_mon, t.tm_year, t.tm_hour, t.tm_min, t.tm_sec)

    """
    Return weather information entry as JSON string
    """

    def toJSON(self):
        data = {"station_name": self.__station_name,
                "tstamp": self.__tstamp,
                "country": self.__country,
                "temp": self.__temp,
                "temp_max": self.__temp_max,
                "temp_min": self.__temp_min,
                "feels_like": self.__feels_like,
                "pressure": self.__pressure,
                "humidity": self.__humidity,
                "wind_speed": self.__wind_speed,
                "wind_deg": self.__wind_deg,
                "clouds_all": self.__clouds_all,
                "rain1h": self.__rain1h,
                "rain3h": self.__rain3h,
                "snow1h": self.__snow1h,
                "snow3h": self.__snow3h,
                "visibility": self.__visibility,
                "sunrise": self.__sunrise,
                "sunset": self.__sunset,
                "main": self.__main,
                "description": self.__description}

        return data
