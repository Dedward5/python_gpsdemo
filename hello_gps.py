# Most basic GPS demo

# From http://www.catb.org/gpsd/gpsd_json.html

import os
from gps3 import gps3
gps_socket = gps3.GPSDSocket()
data_stream = gps3.DataStream()
gps_socket.connect()
gps_socket.watch()
for new_data in gps_socket:
    if new_data:
        data_stream.unpack(new_data)
        print('Altitude = ', data_stream.TPV['alt'])
        print('Latitude = ', data_stream.TPV['lat'])
        print('Longitude = ', data_stream.TPV['lon'])
        print('Speed m/s = ', data_stream.TPV['speed'])
#        print('Status  = ', data_stream.TPV['status'])



data_stream = gps3.DataStream()
