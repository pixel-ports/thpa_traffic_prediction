import pandas as pd

def aggregation_functionVessels(a):

    vessels_data = pd.DataFrame()


    vessels_data = pd.read_csv('thpa_vessels_count.csv')

    parameter = str(a) + "Min"

    vessels_data = vessels_data.drop('Unnamed: 0', axis=1)

    vessels_data['Timestamp'] = pd.to_datetime(vessels_data['date'], format='%Y-%m-%d %H:%M:%S')
    vessels_data['Timestamp'] = vessels_data['Timestamp'].map(lambda x: x.replace(second=0))
    
    vessels_data.set_index('Timestamp', inplace = True)
    vessels_data = vessels_data.groupby(pd.Grouper(freq=parameter)).mean()


    return vessels_data


if __name__ == "__main__":
    data = aggregation_functionVessels(60)
    print (data)