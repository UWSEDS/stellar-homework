"""pronto_utils.py"""

import wget
import os
import zipfile
import pandas as pd
import subprocess

import matplotlib.pyplot as plt
import seaborn; seaborn.set()  # for plot stylings


import urllib3
import os
from urllib3.exceptions import MaxRetryError, LocationValueError
#HTTPError, TimeoutError

def download_if_needed(url, filename):
    """
    Download from URL to filename unless filename already exists
    """
    if os.path.exists(filename):
        filenameExists=(filename, 'already exists')
        return filenameExists
    elif filename:
        import requests
        urllib3.disable_warnings()
        try:
            connection_pool = urllib3.PoolManager(retries=urllib3.Retry(5))
            resp = connection_pool.request('GET',url,timeout=urllib3.Timeout(total=5.0))
            f = open(filename, 'wb')
            f.write(resp.data)
            f.close()
            resp.release_conn()
            downloadSuccessful=('Downloading', filename)
            return(downloadSuccessful)
        except MaxRetryError as e:
            exception='Could not connect to server. Please check to make sure the URL is valid and try again.'
            return exception
        except LocationValueError as e:
            exception=str(e)
            return exception
    else:
        warningMessage='Please input a correct filename.'
        return warningMessage

def remove_data():
    """
    Remove data from __pycache__ and also remove any .csv or .zip files
    """
    if os.path.exists('*.zip') or os.path.exists('__pycache__') or os.path.exists('*.csv'):
        subprocess.call(['./removeCachedData.sh'])
        cacheDelete='Cache and/or .zip folder successfully deleted.'
        return cacheDelete
    else:
        cacheNotDeleted='No cache or .zip folder detected.'
        return cacheNotDeleted



def get_pronto_data():
    """
    Download pronto data, unless already downloaded
    """
    download_if_needed('https://s3.amazonaws.com/pronto-data/open_data_year_one.zip',
                       'open_data_year_one.zip')


def get_trip_data():
    """
    Fetch pronto data (if needed) and extract trips as dataframe
    """
    get_pronto_data()
    zf = zipfile.ZipFile('open_data_year_one.zip')
    file_handle = zf.open('2015_trip_data.csv')
    return pd.read_csv(file_handle)


def get_weather_data():
    """
    Fetch pronto data (if needed) and extract weather as dataframe
    """
    get_pronto_data()
    zf = zipfile.ZipFile('open_data_year_one.zip')
    file_handle = zf.open('2015_weather_data.csv')
    return pd.read_csv(file_handle)


def get_trips_and_weather():
    """
    Combines trip and weather pronto data
    """
    trips = get_trip_data()
    weather = get_weather_data()

    # This is a nice way to access date info in a column
    date = pd.DatetimeIndex(trips['starttime'])

    # pivot table = two-dimensional groupby
    trips_by_date = trips.pivot_table('trip_id', aggfunc='count',
                                      index=date.date, columns='usertype')

    weather = weather.set_index('Date')
    weather.index = pd.DatetimeIndex(weather.index)
    weather = weather.iloc[:-1]
    return weather.join(trips_by_date)


def plot_daily_totals():
    """
    Plot daily ride totals for short-term and annual members
    """
    data = get_trips_and_weather()
    if not data.empty:
        fig, ax = plt.subplots(2, figsize=(14, 6), sharex=True)
        data['Annual Member'].plot(ax=ax[0], title='Annual Member')
        data['Short-Term Pass Holder'].plot(ax=ax[1], title='Short-Term Pass Holder')
        fig.savefig('daily_totals.png')
        plotSuccessful='Daily totals were plotted.'
        return plotSuccessful
    else:
        plotNotSuccessful='Trip and weather data not present.'
        return plotNotSuccessful
