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
from bson.json_util import dumps
from modules.mongodriver import MongoDriver
from credentials import *

try:
    mongo = MongoDriver(db_host, db_port, db_name, db_user, db_pass)

    for location in glb_locations:
        print("> Export all collections for '{0}'".format(location))
        formattedLocation = mongo.generateCollectionName(location)
        cursor = mongo.getAllRawAsList(formattedLocation)
        list_cursor = list(cursor)
        json_data = dumps(list_cursor, indent=2)
        with open("{0}.json".format(formattedLocation), 'w') as outfile:
            outfile.write(json_data)

except Exception as err:
    print("[ERROR] {0}".format(err))
