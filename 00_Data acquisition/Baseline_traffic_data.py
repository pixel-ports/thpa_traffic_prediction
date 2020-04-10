import json
import time
import pandas as pd
import requests


url = "https://download.thpa.gr/pixel/traffic.php?dd="

date = pd.to_datetime("2018-9-1")
all_traffic = pd.DataFrame()
try:
    while date < pd.to_datetime("2020-02-25"):
        print(date.strftime("%d/%m/%Y"))
        response = requests.request("GET", url + date.strftime("%d/%m/%Y"))

        response_df = pd.DataFrame(response.json())
        response_df.to_csv(f'../data/raw/{date.date()}.json', index=False)

        one_day_entries_df = pd.DataFrame()
        one_day_exits_df = pd.DataFrame()

        one_day_entries_df["timestamp"] = pd.to_datetime(response_df["entry_time"], format="%d/%m/%Y %H:%M:%S")
        one_day_entries_df["location_id"] = response_df["entry_gate"]
        one_day_entries_df["id"] = response_df["id"]

        one_day_exits_df["timestamp"] = pd.to_datetime(response_df["exit_time"], format="%d/%m/%Y %H:%M:%S")
        one_day_exits_df["location_id"] = response_df["exit_gate"]
        one_day_exits_df["id"] = response_df["id"]

        all_traffic = pd.concat([all_traffic, one_day_entries_df, one_day_exits_df])

        date += pd.to_timedelta("1 d")
        time.sleep(3)
except Exception as e:
    print(e)

all_traffic = all_traffic.dropna().drop_duplicates()
print(len(all_traffic))
#all_traffic = all_traffic.drop(columns=["id"])
all_traffic.to_csv("../data/thpa_traffic_sept18.csv")
#all_traffic.reset_index(drop=True).to_feather("../data/thpa_traffic.feather")
