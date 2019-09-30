#!/usr/bin/python

import pandas as pd
import requests as requests
import json
import ijson
import sys
import datetime
from datetime import timedelta
import numpy as np
import time
import csv


#Instantiating and giving value to the interval that wants to be converted into the baseline format
date = sys.argv[1]
time_start = sys.argv[2]
time_end = sys.argv[3]
initial_composed_date = date + " " + time_start
print(initial_composed_date)
final_composed_date = date + " " + time_end
print(final_composed_date)
interval = sys.argv[4]
int_seconds = int(interval)*60


initial_date_time_obj = datetime.datetime.strptime(initial_composed_date, '%d/%m/%Y %H:%M:%S')
print(initial_date_time_obj)
final_date_time_obj = datetime.datetime.strptime(final_composed_date, '%d/%m/%Y %H:%M:%S')
print(final_date_time_obj)

#Calculate how many rows must the out_csv have
d1_ts = time.mktime(final_date_time_obj.timetuple())
d2_ts = time.mktime(initial_date_time_obj.timetuple())
diff_minutes = int(d1_ts-d2_ts) / 60
print(diff_minutes)
out_csv_rows = int(diff_minutes / int(float(interval)))+1
print(out_csv_rows)

#Making the call to the server where the Historical Data is stored
#The call is made to the URL with the date (format accepted by the web service)
raw_data = requests.get("https://download.thpa.gr/pixel/traffic.php?dd="+date).text
raw_data = raw_data[3:-44]
raw_data.replace('" ""', '')
#raw_data.replace("" "",'"')
print(raw_data[239])
print(raw_data[240])
print(raw_data[241])
print(raw_data[262])

data = []
def ParseIncomingData(message): #https://stackoverflow.com/questions/54405138/parse-list-of-json-string-in-python
    n = 11
    frames = message.split(',')
    while frames:
        y= ','.join(frames[:n])
        frames = frames[11:]
        data.append(y)
        #print (y)
    return data

data = ParseIncomingData(raw_data)


print("\n")
print(len(data))

def volume(list, gate_operation): #list -- data, operation is entry or exit, gate is 16 or 10A, mc is minute_constructor , if is interval factor
    counter = [0]*out_csv_rows
    for n in range(1,len(list)-1):
        jdata = json.loads(list[n])
        #print(jdata["entry_gate"])
        #print(jdata["exit_gate"])
        #print("\n")
        if (gate_operation in jdata["entry_gate"]) or (gate_operation in jdata["exit_gate"]):
            #print("The conditional sentence of gate works well!")
            this_entry_time = this_time=datetime.datetime.strptime(jdata["entry_time"], '%d/%m/%Y %H:%M:%S')
            this_exit_time = this_time=datetime.datetime.strptime(jdata["exit_time"], '%d/%m/%Y %H:%M:%S')
            print("Entry_time: "+str(this_entry_time))
            print("Exit_time: "+str(this_exit_time))
            print("----")

            for i in range(0, out_csv_rows):
                if i != 0:
                    minute_prev = timedelta(minutes=(int(interval)*(i-1)))
                else:
                    minute_prev = timedelta(minutes=(int(interval)*i))
                minute = timedelta(minutes=(int(interval)*i)-1)
                print("Initial time of the iteration:"+str(initial_date_time_obj+minute_prev))
                print("Initial time + delta of iteration"+str(initial_date_time_obj+minute))
                print("\n")
                if i != 0:
                    if ( (initial_date_time_obj+minute_prev) < this_entry_time < (initial_date_time_obj+minute) ) or ( (initial_date_time_obj+minute_prev) < this_exit_time < (initial_date_time_obj+minute) ):
                        counter[i] = counter[i]+1
                        print("New coincidence: ---  Vehicle through: "+gate_operation)
                else:
                    if ( initial_date_time_obj+minute < this_entry_time < (initial_date_time_obj+minute) ) or ( initial_date_time_obj < this_exit_time < (initial_date_time_obj+minute) ):
                        counter[i] = counter[i]+1
                        print("New coincidence: ---  Vehicle through: "+gate_operation)
    return counter


c10a = volume(data,"Gate 10A")
c16 = volume(data,"Gate 16")


#Creating the csv
file = open("OBJ1_DATASET.csv", "a")
csvWriter = csv.writer( file )

for i in range(0,out_csv_rows):
    minute_constructor = timedelta(seconds=int_seconds*i)
    csvWriter.writerow( [initial_date_time_obj+minute_constructor, c10a[i], "Gate 10A"] )
    csvWriter.writerow( [initial_date_time_obj+minute_constructor, c16[i], "Gate 16"] )
file.close()
