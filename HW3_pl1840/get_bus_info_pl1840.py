from __future__ import print_function
import pylab as pl
import os
import json
import sys
import csv
try:
	import urllib2 as urllib
except ImportError:
	import urllib.request as urllib

key = sys.argv[1]
line = sys.argv[2]

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + key + "&VehicleMonitoringDetailLevel=calls&LineRef=" + line
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

bus=len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])

BUS_Line = sys.argv[3]
bus_line = open(BUS_Line, "w")
bus_line.write("Latitude, Longitide, Stop Name, Stop Status\n")

for n in (range(0, bus)):
	latitude=data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][n]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
	longitude=data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][n]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
	try:
		stop = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][n]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
	except:
		stop = "N/A"
	try:
		status = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][n]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
	except:
		status = "N/A"
	bus_line.write("%s,%s,%s,%s\n" %(latitude,longitude,stop,status))

bus_line.close()

