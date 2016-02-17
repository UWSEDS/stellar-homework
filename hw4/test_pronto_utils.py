''' Unit tests for pronto_utils.py '''

import unittest
import os
from pronto_utils import*

class testProntoUtils(unittest.TestCase):
    def testDownloadIfNeeded(self):
        result=download_if_needed('url','aDataset.zip')
        expected_explanation="url does not exist or the server is not responding"
        self.assertEqual(result,expected_explanation)
        self.assertFalse(os.path.exists('aDataset.zip'))
        result=download_if_needed('https://s3.amazonaws.com/pronto-data/open_data_year_one.zip',
                       'open_data_year_one.zip')
        if os.path.exists('open_data_year_one.zip'):
            expected_explanation= "open_data_year_one.zip already exists"
        else:
            expected_explanation="downloading open_data_year_one.zip"
        self.assertEqual(result,expected_explanation)
        self.assertTrue(os.path.exists('open_data_year_one.zip'))

    def testRemoveData(self):
        result=remove_data('aDataset.zip')
        expected_explanation='aDataset.zip'+' does not exist'
        self.assertEqual(result,expected_explanation)
        self.assertFalse(os.path.exists('aDataset.zip'))

        download_if_needed('https://s3.amazonaws.com/pronto-data/open_data_year_one.zip',
                       'open_data_year_one.zip')
        result=remove_data('open_data_year_one.zip')
        expected_explanation='open_data_year_one.zip'+' data is removed'
        self.assertEqual(result,expected_explanation)
        self.assertFalse(os.path.exists('open_data_year_one.zip'))

    def testPlotDailyTotals(self):
        result=plot_daily_totals()
        self.assertTrue(os.path.exists('daily_totals.png'))
        expected_explanation='Plotting Annual Member and Short-Term Pass Holder'
        self.assertEqual(result,expected_explanation)

if __name__ == '__main__':
    unittest.main()
