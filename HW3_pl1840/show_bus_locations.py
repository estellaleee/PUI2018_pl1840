import pylab as pl
import os
import json
import sys
try:
	import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

pl.rc('font', size=15)

key = sys.argv[1]
line = sys.argv[2]

#defining URL to obtain the information from MTA API
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + key + "&LineRef=" + line
response = urllib.urlopen(url)
#reading the response from the site and decoding it to UTF-8 format
data = response.read().decode("utf-8")
#converting the file to json format
data = json.loads(data)

bus=len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])
for n in range(bus):
	latitude=data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][n]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
	longitude=data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][n]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
	print ("Bus %s is at latitude %s and longitude %s" %(n+1, latitude, longitude))


