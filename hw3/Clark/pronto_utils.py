import wget
import os
import zipfile
import pandas as pd

def download_if_needed(URL,filename):
    """
    Download from URL to filename unless the filename already exists
    """
    if os.path.exists(filename):
        print(filename,'already exists!')
        return
    else:
        wget.download(URL)
        print('Downloading...',filename)
        
def get_pronto_data():
    """
    Download pronto data if it is not already on your computer
    """
    download_if_needed('https://s3.amazonaws.com/pronto-data/open_data_year_one.zip','open_data_year_one.zip')
    
def get_trip_data():
    """
    Fetch pronto data (if needed) and extract trip data as a dataframe
    """
    get_pronto_data()
    zf = zipfile.ZipFile('open_data_year_one.zip')
    file_handle=zf.open('2015_trip_data.csv')
    return pd.read_csv(file_handle)

def get_weather_data():
    """
    Fetch pronto data (if needed) and extract weather data as a dataframe
    """
    get_pronto_data()
    zf = zipfile.ZipFile('open_data_year_one.zip')
    file_handle=zf.open('2015_weather_data.csv')
    return pd.read_csv(file_handle)

def get_trips_and_weather():
    """
    Extracts trip and weather data and then joins them into one dataframe
    """
    trips=get_trip_data()
    weather=get_weather_data()

    date=pd.DatetimeIndex(trips['starttime'])

    trips_by_date_gender=trips.pivot_table('trip_id',aggfunc='count',index=date.date,columns='gender')
    trips_by_date_usertype=trips.pivot_table('trip_id',aggfunc='count',index=date.date,columns='usertype')
    trips_by_date_triplength=trips.groupby(date.date)['tripduration'].mean()
    
    weather=weather.set_index('Date')

    weather.index=pd.DatetimeIndex(weather.index)

    weather=weather.join(trips_by_date_usertype)
    weather=weather.join(trips_by_date_gender)
    weather=weather.join(trips_by_date_triplength)
    weather=weather.iloc[:-1]
    
    weather['tripduration']=weather['tripduration']/60

    return weather
