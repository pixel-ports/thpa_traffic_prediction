import pandas as pd
import ast



def aggregation_functionWeather(a):

    weather_data = pd.DataFrame()
    weather_data = pd.read_csv('weather_data.csv')
    '''
    for index, row in df.iterrows():
        darkSky = row['darkSkyPireaus']
        dict_darkSky = ast.literal_eval(darkSky)
        currently = dict_darkSky['currently']
        
        weather_data = weather_data.append(currently, ignore_index = True)
    weather_data['time'] = weather_data['time'].apply(lambda x: pd.Timestamp(x, unit = 's'))
    weather_data = weather_data.drop_duplicates()
    
    weather_data['time'] = pd.to_datetime(weather_data['time'], format='%Y-%m-%d %H:%M:%S')
    weather_data['time'] = weather_data['time'].map(lambda x: x.replace(second=0))
    a = str(a) + 'Min'
    weather_data.set_index('time', inplace = True)
    weather_data = weather_data.groupby(pd.Grouper(freq=a)).mean()
    '''
    parameter = str(a) + "Min"
    weather_data['timestamp'] = pd.to_datetime(weather_data['timestamp'], format='%Y-%m-%d %H:%M:%S')
    weather_data['timestamp'] = weather_data['timestamp'].map(lambda x: x.replace(second=0))
    
    weather_data.set_index('timestamp', inplace = True)
    weather_data = weather_data.groupby(pd.Grouper(freq=parameter)).mean()
    

    return weather_data