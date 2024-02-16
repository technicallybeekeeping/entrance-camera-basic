#!/usr/bin/env python
""" This simple script takes a basic photo for the Raspberry Pi.
___ ____ ____ _  _ _  _ _ ____ ____ _    _   _   _   ___  ____ ____ _  _ ____ ____ ___  _ _  _ ____
 |  |___ |    |__| |\ | | |    |__| |    |    \_/    |__] |___ |___ |_/  |___ |___ |__] | |\ | | __
 |  |___ |___ |  | | \| | |___ |  | |___ |___  |     |__] |___ |___ | \_ |___ |___ |    | | \| |__]
                                                                                                      
This file is part of the Entrance Camera Basic distribution 
(https://github.com/technicallybeekeeping/entrance-camera-basic).

Copyright (c) 2024 Technically Beekeeping, LLC
This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.

Want to learn more?!? 
See https://www.youtube.com/@TechnicallyBeekeeping or https://technicallybeekeeping.com
"""
from picamera2 import Picamera2
import datetime as dt

# Variables
dateStr = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
path = "./photos/basic_photo_1-" + "-" + dateStr + ".jpg"

# Camera
cam = Picamera2()
cam.start_and_capture_file(path)

# TODO: Let's build more AWESOMENESS ＼(^o^)／ in a future video https://www.youtube.com/@TechnicallyBeekeeping 