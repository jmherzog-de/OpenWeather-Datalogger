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

from flask import Flask, render_template
from modules.mongodriver import MongoDriver
from modules.weather import Weather

# database parameters
db_host = '127.0.0.1'
db_port = '27017'
db_user = '#'
db_pass = '#'

def getLastEntry(location):
    try:
        mongo = MongoDriver(db_host, db_port, db_user, db_pass)
        return mongo.getLastEntry(location)
    except Exception as err:
        print(f'{err}')
        return []

def get_station_data(location):

    try:
        # initialize database
        mongo = MongoDriver(db_host, db_port, db_user, db_pass)

        entries = mongo.getAll(location)

        entry_list = []

        for x in entries:
            entry = Weather()
            entry.set_temp(x['temp'])
            entry.set_temp_max(x['temp_max'])
            entry.set_temp_min(x['temp_min'])
            entry.set_feels_like(x['feels_like'])
            entry.set_pressure(x['pressure'])
            entry.set_humidity(x['humidity'])
            entry.set_wind_speed(x['wind_speed'])
            if x['wind_deg'] != None:
                entry.set_wind_deg(float(x['wind_deg']))
            entry.set_clouds_all(x['clouds_all'])
            if x['rain1h'] != None:
                entry.set_rain1h(x['rain1h'])
            if x['rain3h'] != None:
                entry.set_rain3h(x['rain3h'])
            if x['snow1h'] != None:
                entry.set_snow1h(x['snow1h'])
            if x['snow3h'] != None:
                entry.set_snow3h(x['snow3h'])
            if x['visibility'] != None:
                entry.set_visibility(x['visibility'])
            entry.set_sunrise(x['sunrise'])
            entry.set_sunset(x['sunset'])
            entry.set_main(x['main'])
            entry.set_description(x['description'])
            entry.set_tstamp(x['tstamp'])

            entry_list.append(entry)
        # end of foor loop

        return entry_list
    except Exception as err:
        print(f'{err}')
        return []

app = Flask(__name__)

@app.route('/')
def index():
    lastData = {'Heilbronn': getLastEntry('Heilbronn'), 'Schwäbisch Hall': getLastEntry('Schwäbisch Hall'), 'Vellberg': getLastEntry('Vellberg'), 'Schrozberg': getLastEntry('Schrozberg'), 'Würzburg': getLastEntry('Würzburg'), 'Stuttgart': getLastEntry('Stuttgart'), 'Schwäbisch Hall': getLastEntry('Schwäbisch Hall')}
    return render_template('index.html', title='Wetterdaten', locationData=lastData)

@app.route('/location/<name>')
def locationRoute(name):
    if name == None:
        name = 'Vellberg'
    
    locData = get_station_data(name)
    locData.reverse()
    return render_template('location.html', title='Wetterdaten', locationData=locData, location=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1024, debug=True)