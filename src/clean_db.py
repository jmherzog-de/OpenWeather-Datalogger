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

from modules.mongodriver import MongoDriver
from credentials import *

try:
    mongo = MongoDriver(db_host, db_port, db_name, db_user, db_pass)

    for location in glb_locations:
        mongo.dropCollection(location)
        print(
            "> Collection for location '{0}' dropped successfully.".format(
                location)
        )
except Exception as err:
    print("[ERROR] {0}".format(err))
