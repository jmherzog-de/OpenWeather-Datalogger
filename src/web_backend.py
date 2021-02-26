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
from credentials import *

"""
return last entry from database collection for
a specific location as a Weather object.
"""

def getLastEntry(location):
    try:
        mongo = MongoDriver(db_host, db_port, db_name, db_user, db_pass)
        # return of mongo.getRows() has type list
        return mongo.getRows(location, limit=1, DESC=True, format=True)[0]
    except Exception as err:
        print(f'{err}')
        return None


"""
return all entries from database collection for
a specific location as a list of Weather objects.
"""
def getStationData(location):

    try:
        mongo = MongoDriver(db_host, db_port, db_name, db_user, db_pass)
        return mongo.getRows(location, limit=96, DESC=True, format=True)
    except Exception as err:
        print(f'{err}')
        return []

app = Flask(__name__)

@app.route('/')
@app.route('/location')
def index():

    """
    generate list of all locations for
    last database entries.
    """
    lastData = {}
    for station in glb_locations:
        lastData[station] = getLastEntry(station)

    return render_template('index.html', title='Wetterdaten', locationData=lastData, location="", locations=glb_locations)

@app.route('/location/<name>')
def locationRoute(name):
    locData = getStationData(name)
    return render_template('location.html', title='Wetterdaten', locationData=locData, location=name, locations=glb_locations)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1024, debug=True)
