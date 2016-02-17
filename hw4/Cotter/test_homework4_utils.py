import unittest
import homework4_utils as utils
import os
import glob


class testHomework4_utils(unittest.TestCase):

    def testDownload_if_needed(self):

        # assert that a bad URL raises the expected error
        self.assertRaises(FileNotFoundError, utils.download_if_needed,
                            'http://badurl.com/badData.zip','badData.zip')

        # assert that a good URL raises no error
        try:
            downloadedTest = utils.download_if_needed('https://s3.amazonaws.com/pronto-data/open_data_year_one.zip',
                               'open_data_year_one.zip')
        except:
            self.fail("download_if_needed failed to download valid URL. This is possibly due to a bad internet connection.")

        # assert that data was downloaded
        dataDownloaded = os.path.exists('open_data_year_one.zip')
        self.assertTrue(dataDownloaded)


    def testPlot_daily_totals(self):

        try:
            utils.plot_daily_totals()
            fileExists = os.path.exists('daily_totals.png')
            self.assertTrue(fileExists)
        except:
            self.fail("Error during execution of plot_daily_totals")

    def testRemove_data(self):
        # do not need to create zip/csv files, because if
        # this far in the test, data will already be downloaded
        utils.remove_data()
        CSVremoved = not glob.glob('*.csv')
        ZIPremoved = not glob.glob('*.zip')

        self.assertTrue(CSVremoved)
        self.assertTrue(ZIPremoved)

if __name__ == '__main__':
    unittest.main()
