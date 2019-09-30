#!/usr/bin/python

import datetime
from datetime import timedelta
import time
import csv
import os
import sys


#Instantiating and giving value to the interval that wants to be converted into the baseline format
date_start = sys.argv[1]
time_start = sys.argv[2]
date_end = sys.argv[3]
time_end = sys.argv[4]
interval = sys.argv[5]


initial_date_obj = datetime.datetime.strptime(date_start, '%d/%m/%Y')
print("Initial date of multiple days: "+str(initial_date_obj))
final_date_obj = datetime.datetime.strptime(date_end, '%d/%m/%Y')
print("Final date of multiple days: "+str(final_date_obj))
print("-----")

#Calculate how many days there are between date_start and date_end -- equal to the number of calls to objective1_oneday.py
delta = final_date_obj - initial_date_obj
calls = delta.days+1
print("Number of calls to the one-day script: "+str(calls))

#Creating the csv file
file = open("OBJ1_DATASET.csv", "w+")
csvWriter = csv.writer( file )
#csvWriter.writerow( ["timestamp", "volume", "location"] ) #header of the CSV

#Make the proper calls to objective1_oneday.py
os.system("objective1_oneday.py "+date_start+" "+time_start+" 23:59:59 "+interval)
for n in range(1,calls-1):
    date_x= initial_date_obj+timedelta(days=n)
    print("The date_x for the iteration:"+str(n)+" is:"+str(date_x))
    date_x_str =str(date_x.day)+"/"+str(date_x.month)+"/"+str(date_x.year)
    os.system("objective1_oneday.py "+date_x_str+" 00:00:01 23:59:59 "+interval)

os.system("objective1_oneday.py "+date_end+" 00:00:01 "+time_end+" "+interval)
