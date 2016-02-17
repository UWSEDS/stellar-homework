import unittest
import os
from pronto_utils import download_if_needed, plot_daily_totals, remove_data

class ProntoUtilsTester(unittest.TestCase):

        def testDownloadIfNeeded(self):
            """
            Test the data download function in the case of both an invalid
            and valid URL. In the former case, we check to see that the data
            file does not exist (since the link was invalid); in the latter,
            we check that the data file does exist.
            """

            validURL = 'https://s3.amazonaws.com/pronto-data/open_data_year_one.zip'
            invalidURL = 'ttps://s3.amazonaws.com/pronto-data/open_data_year_one.zip'
            fileName = 'open_data_year_one.zip'
            path = os.getcwd() + '\open_data_year_one.zip'

            # invalid url
            download_if_needed(invalidURL,fileName)
            self.assertFalse(os.path.exists(path))

            # valid url
            download_if_needed(validURL,fileName)
            self.assertTrue(os.path.exists(path))

        def testPlotDailyTotals(self):
            """
            Test the plot_daily_totals function by seeing if the plot was
            created (i.e., the corresponding .png image file exists)
            """

            plot_daily_totals()
            plotPath = os.getcwd() + '\daily_totals.png'
            self.assertTrue(os.path.exists(plotPath))

        def testRemoveData(self):
            """
            Test the remove_data function by seeing if the data was deleted
            from the directory
            """

            remove_data()
            cwd = os.getcwd()
            path = cwd + '\open_data_year_one.zip'

            # the zip file
            self.assertFalse(os.path.exists(path))

            # individual .csv and .txt files uncase unzipped
            self.assertFalse(os.path.exists(cwd + '\\2015_station_data.csv'))
            self.assertFalse(os.path.exists(cwd + '\\2015_status_data.csv'))
            self.assertFalse(os.path.exists(cwd + '\\2015_trip_data.csv'))
            self.assertFalse(os.path.exists(cwd + '\\2015_weather_data.csv'))
            self.assertFalse(os.path.exists(cwd + '\README.txt'))


if __name__ == '__main__':
    unittest.main()
