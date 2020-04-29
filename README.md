## - THPA TRAFIC PREDICTION -

Below there are the project structure and content summary used for the road traffic data prediction algorithm in THPA. PIXEL project (H2020 GA. No 769355).

---

## 00_Data Collection
Python scripts in charge of collecting base information about the status of traffic and additional attributes like weather or vessel calls, useful for training and developing the predictive models.

- **Baseline information** about the status of traffic:

	- THPA gate volume data

- **Additional attributes**: 

	- **Other traffic datasources**:
	    - TrafficThess IMET 
	    - IMET (open data)

	-	**Ship calls**: THPA vessel calls webservice

    - **Weather**:
			- Stratus meteo data    

---

## 01_Data Preparation

Files (.CSV) coming from the Data Collection scripts are treated, filtered and provided as an output in two formats (per request). The results are .csv files containing the information wanted (editable by the user) adjusted for:

 - Common baseline data format: _[timestamp, volume/speed, location]_
 - Prepared for Facebook Prophet framework: _[index, timestamp, vol_location]_

---

## 02_EDA

This directory contains Exploratory Data Analysis Jupyter notebooks. This is for discovering trends, pattern, seasonalities and external factors that may influence traffic volume.

---

## 03_Models

Scripts for **predicting volume/speed** at **one location** at **one moment of time** with a 60-minutes granularity. The base models are selected out of the **state of the art** analysis, then the models are **trained** with the historical data collected in the previous steps (Data Preparation) and finally they are **fine-tuned** to be adapted to the use-case and requirements.

## data
CSVs with the data used for creating and using the models.

For acquiring the weather data, specific written consent must be gathered from the data owners. Reference: http://penteli.meteo.gr/stations/helexpo/  -- Terms of use: https://www.meteo.gr/terms.cfm

For gathering City traffic data (only research purposes), https://www.trafficthess.imet.gr/ must be visited. Reference must be done to: http://opendata.imet.gr/about  - Check terms of use.

---
