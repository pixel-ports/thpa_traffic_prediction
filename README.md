# - THPA TRAFIC PREDICTION v1 -

Below there is the project files explanation.

---

## Files
Python scripts in charge of collecting base information fromg THPA RFID sensors in gates 16 and 10A of the port.

The objective of these scripts are to retrieve the raw information from the THPA webservice (https://download.thpa.gr/pixel) and to filter the response according to adjustable parameters.

- **objective1_oneday**: Considering that the service needs to be called once per each day, this sub-script will be used for retrieving an interval within one day. The script accepts arguments through console (argvs): _Date, start time, end time and interval (in minutes)_.

- **objective1_multipledays**: If the interval comprehends more than one day (usual case) this script will need to be used. The script accepts arguments through console (argvs): _Start date, start time, end date, end time and interval (in minutes)_.

- **OBJ1_DATASET.csv : The output is a .CSV formatted with the agreed baseline common data format: _[timestamp, volume, location_id]_. Where location_id are the coordinates of gates 16 and 10A of Thessaloniki port and volume is the number of vehicles entering/exiting that gate in the corresponding interval.


---

## Comments

The scripts must be run in Linux/Windows environments with Python and pip installed and with the following dependencies (packages): _pandas, requests, ijson, json, datetime, sys, os, numpy, time_ and _csv_ .
