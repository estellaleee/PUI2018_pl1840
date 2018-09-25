import pylab as pl
import os
import json
import sys
try:
	import urllib2 as urllib
except ImportError:
    import urllib.request as urllib


key = sys.argv[1]
line = sys.argv[2]


url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + key + "&LineRef=" + line
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

bus=len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])
print ("Bus Line: " + line)
print ("Number of Active Buses:%s"%(bus))
for n in range(bus):
	latitude=data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][n]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
	longitude=data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][n]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
	print ("Bus %s is at latitude %s and longitude %s" %(n+1, latitude, longitude))


