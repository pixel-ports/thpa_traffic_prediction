## 1_Data Collection

Python scripts in charge of collecting base information about the status of traffic and additional attributes like weather or vessel calls, useful for training and developing the predictive models.

- **Baseline information** about the status of traffic:

	- **THPA gate volume data**: RFID sensors for entry/exit vehicles in gates 10A and 16. This information is provided by THPA through a webservice (download.thpa.gr/pixel) in which we can obtain the full sheet of vehicles entering and exiting the port of one day. For the historical data collection (aiming at training the model), several days can be collected (till back to April-2018). For the current entries/exits, the "today" register contains the vehicles up to the daytime when it is called (aiming at performing the model).
      - _Output_:  List of entries/exits of both gates in one day


- **Additional attributes**: ** TO - DO**

	- **Other traffic datasources**:
	    - **TrafficThess (open data)**:
	      - _Output_:
	    - **IMET (open data)**:
	      - _Output_:
	-	**Ship calls**:
		- **THPA vessel calls webservice**.
	      - _Output_:

  - **Weather**:
	- **Weather station in THPA**
      - _Output_
	- **DarkSky API**------------------------------> Weather Table Data
      - _Output_:
