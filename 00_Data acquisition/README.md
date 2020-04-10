## 00_Data Collection

Python scripts in charge of collecting base information about the status of traffic and additional attributes like weather or vessel calls, useful for training and developing the predictive models.

- **Baseline information** about the status of traffic:

	- **THPA gate volume data**: RFID sensors for entry/exit vehicles in gates 10A and 16. This information is provided by THPA through a webservice created for the project in which we can obtain the full sheet of vehicles entering and exiting the port of one day. For the historical data collection (aiming at training the model), several days can be collected (till back to April-2018). For the current entries/exits, the "today" register contains the vehicles up to the daytime when it is called (aiming at performing the model).
      - _Output_:  [location_id, timestamp, volume traffic]


- **Additional attributes**: 

	- **Other traffic datasources**:
	    - **TrafficThess - IMET (open data)**: Open data (GPS-based) of the city of Thessaloniki. This data (with particular interest in the historic offering) is served by courtesy of CERTH-HIT via the website TrafficThess: https://www.trafficthess.imet.gr . This website has varied information of the different roads of the city (referred as links) updated each 15 minutes, which is perfectly aligned with the used baseline dataset for this task. The procedure followed was: (i) selecting the surrounding links to the gates of THPA, (ii) extracting the data for those 5 links from 28th April 2018 till 5 February 2020, (iii) selecting the interesting fields of the information provided, (iv) building a .csv with the average of the average speeds of the 5 surrounding links.
	      - _Output_: [location_id, timestamp, volume traffic]
	    
	-	**Ship calls**: Data on all the vessels operated by THPA. This data (with particular interest in the historic offering from 2018) is served by IT department of the Port of Thessaloniki via a REST API web created explicitly for PIXEL project. The query to that API returns all the vessels that were operated (one API per year) in a JSON format including very rich information and details of every single vessel in a year. The procedure followed was: (i) downloading every data of all vessels processed in 2018-2020, (ii) fine-tuning the timeframe (28th April 2018 till 5 February 2020), (iii) grouping, filtering and counting the vessels in order to have a .csv prepared with the proper info: number of vessels at berth/maneuvering in the port separated by periods of 60 minutes.	
	  - _Output_: [timestamp, number of vessels at the port]

  - **Weather**:
	- **Weather open data**: For tackling this objective, the team used the free web service provided by Stratus Meteo of Greece: http://stratus.meteo.noa.gr/front . Different sensors are installed throughout Greece and for this case we made use of the one closest to the Port of Thessaloniki.
      - _Output_: [timestamp, temperature, wind_speed, precip_intens]
	
