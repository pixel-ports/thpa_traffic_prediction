import pandas as pd

def aggregation_functionTraffic(a):

    traffic_data = pd.DataFrame()
    traffic_data1 = pd.DataFrame()
    traffic_data2 = pd.DataFrame()
    traffic_data3 = pd.DataFrame()
    traffic_data4 = pd.DataFrame()
    traffic_data5 = pd.DataFrame()

    traffic_data1 = pd.read_csv('csv\\1525_2018-04-27_00_00_2020-02-05_21_29.csv')
    traffic_data2 = pd.read_csv('csv\\2464_2018-04-27_00_00_2020-02-05_21_29.csv')
    traffic_data3 = pd.read_csv('csv\\2545_2018-04-27_00_00_2020-02-05_21_29.csv')
    traffic_data4 = pd.read_csv('csv\\2567_2018-04-27_00_00_2020-02-05_21_29.csv')
    traffic_data5 = pd.read_csv('csv\\2592_2018-04-27_00_00_2020-02-05_21_29.csv')
    '''
    for index, row in df.iterrows():
        darkSky = row['darkSkyPireaus']
        dict_darkSky = ast.literal_eval(darkSky)
        currently = dict_darkSky['currently']
        
        traffic_data = traffic_data.append(currently, ignore_index = True)
    traffic_data['time'] = traffic_data['time'].apply(lambda x: pd.Timestamp(x, unit = 's'))
    traffic_data = traffic_data.drop_duplicates()
    
    traffic_data['time'] = pd.to_datetime(traffic_data['time'], format='%Y-%m-%d %H:%M:%S')
    traffic_data['time'] = traffic_data['time'].map(lambda x: x.replace(second=0))
    a = str(a) + 'Min'
    traffic_data.set_index('time', inplace = True)
    traffic_data = traffic_data.groupby(pd.Grouper(freq=a)).mean()
    '''
    parameter = str(a) + "Min"
    traffic_data1['Timestamp'] = pd.to_datetime(traffic_data1['Timestamp'], format='%Y-%m-%d %H:%M:%S')
    traffic_data1['Timestamp'] = traffic_data1['Timestamp'].map(lambda x: x.replace(second=0))
    
    traffic_data1.set_index('Timestamp', inplace = True)
    traffic_data1 = traffic_data1.groupby(pd.Grouper(freq=parameter)).mean()

    traffic_data1 = traffic_data1.drop(['Link_ID','Free_Flow_Speed','Min_speed','Max_speed','Median_speed','InterquartileMean_speed','GeometricMean_speed','HarmonicMean_speed','Samples','UniqueVehicles'], axis =1)

    traffic_data2['Timestamp'] = pd.to_datetime(traffic_data2['Timestamp'], format='%Y-%m-%d %H:%M:%S')
    traffic_data2['Timestamp'] = traffic_data2['Timestamp'].map(lambda x: x.replace(second=0))
    
    traffic_data2.set_index('Timestamp', inplace = True)
    traffic_data2 = traffic_data2.groupby(pd.Grouper(freq=parameter)).mean()

    traffic_data2 = traffic_data2.drop(['Link_ID','Free_Flow_Speed','Min_speed','Max_speed','Median_speed','InterquartileMean_speed','GeometricMean_speed','HarmonicMean_speed','Samples','UniqueVehicles'], axis =1)

    traffic_data3['Timestamp'] = pd.to_datetime(traffic_data3['Timestamp'], format='%Y-%m-%d %H:%M:%S')
    traffic_data3['Timestamp'] = traffic_data3['Timestamp'].map(lambda x: x.replace(second=0))
    
    traffic_data3.set_index('Timestamp', inplace = True)
    traffic_data3 = traffic_data3.groupby(pd.Grouper(freq=parameter)).mean()

    traffic_data3 = traffic_data3.drop(['Link_ID','Free_Flow_Speed','Min_speed','Max_speed','Median_speed','InterquartileMean_speed','GeometricMean_speed','HarmonicMean_speed','Samples','UniqueVehicles'], axis =1)

    traffic_data4['Timestamp'] = pd.to_datetime(traffic_data4['Timestamp'], format='%Y-%m-%d %H:%M:%S')
    traffic_data4['Timestamp'] = traffic_data4['Timestamp'].map(lambda x: x.replace(second=0))
    
    traffic_data4.set_index('Timestamp', inplace = True)
    traffic_data4 = traffic_data4.groupby(pd.Grouper(freq=parameter)).mean()

    traffic_data4 = traffic_data4.drop(['Link_ID','Free_Flow_Speed','Min_speed','Max_speed','Median_speed','InterquartileMean_speed','GeometricMean_speed','HarmonicMean_speed','Samples','UniqueVehicles'], axis =1)

    traffic_data5['Timestamp'] = pd.to_datetime(traffic_data5['Timestamp'], format='%Y-%m-%d %H:%M:%S')
    traffic_data5['Timestamp'] = traffic_data5['Timestamp'].map(lambda x: x.replace(second=0))
    
    traffic_data5.set_index('Timestamp', inplace = True)
    traffic_data5 = traffic_data5.groupby(pd.Grouper(freq=parameter)).mean()

    traffic_data5 = traffic_data5.drop(['Link_ID','Free_Flow_Speed','Min_speed','Max_speed','Median_speed','InterquartileMean_speed','GeometricMean_speed','HarmonicMean_speed','Samples','UniqueVehicles'], axis =1)
    
    traffic_data = pd.concat([traffic_data1, traffic_data2, traffic_data3, traffic_data4, traffic_data5], axis=1)

    traffic_data['Avg_Speed'] = traffic_data.mean(axis=1)
    traffic_data = traffic_data.drop(['Avg_speed'], axis =1)

    #traffic_data.to_csv('traffic_data.csv')

    return traffic_data


if __name__ == "__main__":
    data = aggregation_functionTraffic(60)
    print (data)