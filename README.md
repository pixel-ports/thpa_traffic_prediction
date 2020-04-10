## - THPA TRAFIC PREDICTION -

Below there are the project structure and content summary used for the road traffic data prediction algorithm in THPA. PIXEL project (H2020 GA. No 769355).

---

## 1_Data Collection
Python scripts in charge of collecting base information about the status of traffic and additional attributes like weather or vessel calls, useful for training and developing the predictive models.

- **Baseline information** about the status of traffic:

	- THPA gate volume data

- **Additional attributes**: ** TO - DO**

	- **Other traffic datasources**:
	    - TrafficThess (open data):
	    - IMET (open data)

	-	**Ship calls**: THPA vessel calls webservice

  - **Weather**:
			- Weather station in THPA    
			- DarkSky API

---

## 2_Data Preparation

Files (.CSV) coming from the Data Collection scripts are treated, filtered and provided as an output in two formats (per request). The results are .csv files containing the information wanted (editable by the user) adjusted for:

 - Common baseline data format: _[timestamp, volume/speed, location]_
 - Prepared for Facebook Prophet framework: _[index, timestamp, vol_location]_

---

## 3_Data Analysis and Discovery

This directory contains Exploratory Data Analysis Jupyter notebooks. This is for discovering trends, pattern, seasonalities and external factors that may influence traffic volume.

---

## 4_Models

Scripts for **predicting volume/speed** at **one location** at **one moment of time**. The base models are selected out of the **state of the art** analysis, then the models are **trained** with the historical data collected in the previous steps (Data Preparation) and finally they are **fine-tuned** to be adapted to the use-case and requirements.

---
