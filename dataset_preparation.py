from __future__ import division
import requests as requests
#import pandas as pd
#from pandas.io.json import json_normalize
from datetime import datetime as dt
import json
import time
import csv


file = open("training_dataset.csv", "a")
csvWriter = csv.writer( file )
headerString = "timestamp,s0,s1,s2,s3,s4,temperature,humidity,visibility,precipitation,cloudcoverage,ozone,CIx"
print(headerString)
csvWriter.writerow(["timestamp","s0","s1","s2","s3","s4","temperature","humidity","visibility","precipitation","cloudcoverage","ozone","CIx"])
file.close()

minutes = [0,15,30,45]
#One point per segment. Location representative useful for retrieving the average values associated to those segments.
points = ["40.647309,22.903674","40.65384,22.89522","40.65995,22.90025","40.653587,22.905174", "40.652107,22.908948"]
s = []

while True:  
	if dt.now().minute in minutes:
		#Getting temperature, humidity and visibility from OpenWeather (point -- target location) 
		openWeatherLoc = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=40.6447719&lon=22.902983&appid=e2a9f31bdc36196db5ce04eaad9afb35&units=metric").json()
	 	#oWLoc = json.loads(openWeatherLoc)
		oWLoc = openWeatherLoc
		temperature = oWLoc["main"]["temp"]
		humidity = oWLoc["main"]["humidity"]
		visibility = oWLoc["visibility"]

		#Getting precipitation level, cloud coverage and ozone from DarkSky (point -- target location)
		darkSkyLoc = requests.get("https://api.darksky.net/forecast/cc316d8a8b29a6117a238d0d7da97ba5/40.6447719,22.902983").json()
		#dSLoc = json.loads(darkSkyLoc)
		dSLoc = darkSkyLoc
		precipitation = dSLoc["currently"]["precipIntensity"]
		cloudcoverage = dSLoc["currently"]["cloudCover"]
		ozone = dSLoc["currently"]["ozone"]

		#Getting traffic current speed and free flow speed per each one of the relevant segments identified in TomTom
		for i in range(0, len(points)):
			 resp = requests.get("https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json?key=f1OlwwAb0Om6qt8vIAWv85bej8mfbMBT&point="+points[i]).json()
			 #rs = json.dumps(resp)
			 #rson = json.loads(resp)
			 rson = resp
		         currentspeed = rson["flowSegmentData"]["currentSpeed"]
			 freeflowspeed = rson["flowSegmentData"]["freeFlowSpeed"]
			 #The value to be included in the dataset is the Congestion Index per segment
			 s.append(currentspeed / freeflowspeed)

		#Get the ground truth value for this moment (CI in the point of interest)
		resp = requests.get("https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json?key=f1OlwwAb0Om6qt8vIAWv85bej8mfbMBT&point=40.6447719,22.902983").json()
                #rson = json.loads(resp)
                rson = resp
		currentspeed = rson["flowSegmentData"]["currentSpeed"]
                freeflowspeed = rson["flowSegmentData"]["freeFlowSpeed"]
                #The value to be included in the dataset is the Congestion Index per segment
                CIx = currentspeed / freeflowspeed


		#Get the current timestamp (to be used as ID_col in the dataset entries)
		timestamp = time.strftime("%x--%I:%M:%S")

		#Add new row in the CSV file with all the information
		file = open("training_dataset.csv", "a")
		csvWriter = csv.writer(file)
		#stringAll =str(timestamp)+","+ str(s[0])+","+str(s[1])+","+str(s[2])+","+str(s[3])+","+str(s[4])+","+str(s[5])+","+str(temperature)+","+str(humidity)+","+str(visibility)+","+str(precipitation)+","+str(cloudcoverage)+","+str(ozone)+","+str(CIx)
		print(str(timestamp))
		print(str(s[0]))
		print(str(s[2]))		
		print(str(s[3]))		
		print(str(s[4]))	
		print(str(humidity))
		print(str(visibility))
		print(str(precipitation))
		print(str(cloudcoverage))
		print(str(ozone))
		print(str(CIx))


		file = open("training_dataset.csv", "a")
		csvWriter = csv.writer( file )
		csvWriter.writerow( [timestamp, s[0], s[1], s[2], s[3], s[4], temperature, humidity, visibility, precipitation, cloudcoverage, ozone, CIx] )
    		file.close()
		time.sleep(120)

	else:pass
