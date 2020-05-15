import pandas as pd

def unifiedModel_TomTom(a):

    #These are the points for which traffic data is requested and will be used as location_id
    points = ['37.948407,23.618734', '37.949056,23.622872', '37.947528,23.626445', '37.951318,23.629970', '37.944304,23.627213', '37.946127,23.633617', '37.943518,23.632879', '37.950339,23.634460', '37.949275,23.638958', '37.949459,23.645260', '37.949591,23.648858', '37.946790,23.645170', '37.942664,23.643054', '37.943530,23.645925', '37.941175,23.645508', '37.938930,23.640589', '37.937748,23.642510', '37.935599,23.635565', '37.937644,23.634318', '37.936736,23.630546']

    #We read the data from the csv generated
    data = pd.read_csv('thpa_traffic_volume_prepared.csv')

    #Do we have to remove rows with confidence lower than a threshold?
    #data = data[data['flowSegmentData.confidence']>0.5]

    #Location_id column is generated from the index column value
    #data['location_id'] = (data['index'].apply(lambda x: points[x]))

    #Only location_id, timestamp and current_speed columns are kept
    #data = data[['location_id','TimeStampUTC','flowSegmentData.currentSpeed']]

    #Rename columns to names defined at ppt
    #data = data.rename(columns={'flowSegmentData.currentSpeed' : 'current_speed', 'TimeStampUTC' : 'timestamp'})

    #Change columns type to correct ones
    data['timestamp'] = pd.to_datetime(data['timestamp'], format='%Y-%m-%d %H:%M:%S')
    data['timestamp'] = data['timestamp'].map(lambda x: x.replace(second=0))
    
    #Remove rows ousssst of time
    data['minute'] = data['timestamp'].dt.minute
    data = data[(data['minute'].isin([0,15,30,45]))]
    data = data.drop(columns = ['minute'])
    
    
    unifiedModel = data
    
    
    return unifiedModel