import json
import time
import pandas as pd
import requests


url18 = "https://download.thpa.gr/pixel/shipcalls.php?y=2018"
url19 = "https://download.thpa.gr/pixel/shipcalls.php?y=2019"
url20 = "https://download.thpa.gr/pixel/shipcalls.php?y=2020"

#date = pd.to_datetime("2018-9-1")
all_vessels = pd.DataFrame()

try:
    response1 = requests.request("GET", url18)
    response_df1 = pd.DataFrame(response1.json())
    response_df1.to_csv(f'./data/2018.json', index=False)
    print("Folder 2018 data created")
    twenty18_correct_df = pd.DataFrame()
    twenty18_correct_df["start_work"] = pd.to_datetime(response_df1["start_work"],  format="%b %d %Y %I:%M:%S:%f%p")
    twenty18_correct_df["end_work"] = pd.to_datetime(response_df1["end_work"], format="%b %d %Y %I:%M:%S:%f%p")
    twenty18_correct_df["imo_code"] = response_df1["imo_code"]
    #format="%b %d %Y %I:%M:%S:%f:%p",

    time.sleep(3)

    response2 = requests.request("GET", url19)
    response_df2 = pd.DataFrame(response2.json())
    response_df2.to_csv(f'./data/2019.json', index=False)
    twenty19_correct_df = pd.DataFrame()
    twenty19_correct_df["start_work"] = pd.to_datetime(response_df2["start_work"], format="%b %d %Y %I:%M:%S:%f%p")
    twenty19_correct_df["end_work"] = pd.to_datetime(response_df2["end_work"], format="%b %d %Y %I:%M:%S:%f%p")
    twenty19_correct_df["imo_code"] = response_df2["imo_code"]

    time.sleep(3)

    response3 = requests.request("GET", url20)
    response_df3 = pd.DataFrame(response3.json())
    response_df3.to_csv(f'./data/2020.json', index=False)
    twenty20_correct_df = pd.DataFrame()
    twenty20_correct_df["start_work"] = pd.to_datetime(response_df3["start_work"], format="%b %d %Y %I:%M:%S:%f%p")
    twenty20_correct_df["end_work"] = pd.to_datetime(response_df3["end_work"], format="%b %d %Y %I:%M:%S:%f%p")
    twenty20_correct_df["imo_code"] = response_df3["imo_code"]

    all_vessels = pd.concat([all_vessels, twenty18_correct_df, twenty19_correct_df, twenty20_correct_df])

except Exception as e:
    print(e)

#Mergin all raw data from 2018, 2019, 2020
all_vessels = all_vessels.dropna().drop_duplicates()
print(len(all_vessels))
all_vessels.to_csv(f"./data/thpa_vessels_raw.csv")

#Preparation of dfs for converting to count values
vessels_csv = "./data/thpa_vessels.csv"
df = pd.read_csv(vessels_csv)
df["start_work"] = pd.to_datetime(df["start_work"])
df["end_work"] = pd.to_datetime(df["end_work"])
df.set_index(["start_work"])

dti = pd.date_range('2018-04-27', periods = 15600, freq='1 H')
dti = pd.DataFrame(dti, columns=["date"])

#Converting the data into a new df with the count values done

vessel_count = []
for index, row in dti.iterrows():
    print(row["date"])
    mask = ((pd.to_datetime(row["date"])>df['start_work']) & (  (pd.to_datetime(row["date"])) <= df['end_work']))
    a = df.loc[mask].count()
    print(a[2])
    vessel_count.append(a[2])

dti["vessel_count"] = vessel_count
dti.to_csv(f"./data/thpa_vessels_count.csv")
