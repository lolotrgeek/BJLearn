# import needed modules
import android
import time
import sys, select, os #for loop exit

#Initiate android-module
droid = android.Android()

#notify me
droid.makeToast("fetching GPS data")

print("start gps-sensor...")
droid.startLocating()

while True:
    #exit loop hook
    if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        line = input()
        print("exit endless loop...")
        break

    #wait for location-event
    event = droid.eventWaitFor('location',10000).result
    if event['name'] == "location":
        try:
            #try to get gps location data
            timestamp = repr(event['data']['gps']['time'])
            longitude = repr(event['data']['gps']['longitude'])
            latitude = repr(event['data']['gps']['latitude'])
            altitude = repr(event['data']['gps']['altitude'])
            speed = repr(event['data']['gps']['speed'])
            accuracy = repr(event['data']['gps']['accuracy'])
            loctype = "gps"
        except KeyError:
            #if no gps data, get the network location instead (inaccurate)
            timestamp = repr(event['data']['network']['time'])
            longitude = repr(event['data']['network']['longitude'])
            latitude = repr(event['data']['network']['latitude'])
            altitude = repr(event['data']['network']['altitude'])
            speed = repr(event['data']['network']['speed'])
            accuracy = repr(event['data']['network']['accuracy'])
            loctype = "net"

        data = loctype + ";" + timestamp + ";" + longitude + ";" + latitude + ";" + altitude + ";" + speed + ";" + accuracy

    print(data) #logging
    time.sleep(5) #wait for 5 seconds

print("stop gps-sensor...")
droid.stopLocating()