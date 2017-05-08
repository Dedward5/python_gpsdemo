from gps3.agps3threaded import AGPS3mechanism
agps_thread = AGPS3mechanism()  # Instantiate AGPS3 Mechanisms
agps_thread.stream_data()  # From localhost (), or other hosts, by example, (host='gps.ddns.net')
agps_thread.run_thread()  # Throttle time to sleep after an empty lookup, default '()' 0.2 two tenths of a second


import os


gps_time = "n/a"

while gps_time == "n/a":  # All data is available via instantiated thread data stream attribute.
    # line #140-ff of /usr/local/lib/python3.5/dist-packages/gps3/agps.py
    print('---------------------')
    print(                   agps_thread.data_stream.time)
    lat = agps_thread.data_stream.alt
    print (lat,)
	#print('Lon:{}   '.format(agps_thread.data_stream.lon))
    #print('Speed:{} '.format(agps_thread.data_stream.speed))
    #print('Course:{}'.format(agps_thread.data_stream.track))
    #print('---------------------')
#    sleep(60) # Sleep, or do other things for as long as you like.
 

    gps_time = agps_thread.data_stream.time
#    gps_date = agps_thread.data_stream.date


    print("time is ",gps_time)

    	
#    print("date is ",gps_date)



print("Final time is ",gps_time)

os.system ('date -s %s' % gps_time )


