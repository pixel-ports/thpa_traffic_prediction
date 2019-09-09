#!/usr/bin/python

import pandas as pd
import requests as requests
import json
import ijson
import sys

#Just printing the list of arguments provided at the execution of the program
print(len(sys.argv))
print('Argument List: ', str(sys.argv))
print(sys.argv[1])

#Instantiating and giving value to the interval that wants to be converted into the baseline format
date = sys.argv[1]
time_start = sys.argv[2]
time_end = sys.argv[3]
interval = sys.argv[4]

#Making the call to the server where the Historical Data is stored --- This should be changed in the future to be read from the PIXEL Information Hub and not directly from
#the raw data source provided by THPA
#The call is made to the URL with the date_start (format accepted by the web service)
raw_data = requests.get("https://download.thpa.gr/pixel/traffic.php?dd="+ date).json()

    #ijson will iteratively parse the json file instead of reading it all in at once.
    #This is slower than directly reading the whole file in, but it enables us to work with
    #large files that can’t fit in memory
with open(raw_data, 'r') as f:
    objects = ijson.items(f,'meta.view.columns.item')
    vehicles = list(objects)
    print(vehicles[0])

#Filtering the data according to the values provided in sys.argv[1 & 2]
#https://www.dataquest.io/blog/python-json-tutorial/
data_json = raw_data

my_new_json
#Calculation of the volume associated to the interval


#Construction of the baseline format (according to the instructions by Dejan)

#Storing the baseline dataset
