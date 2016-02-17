'''Units test for plot_daily_totals.py'''

import unittest
from pronto_utils import plot_daily_totals

class TestPlotTotals(unittest.TestCase):
    #Test if function operates when trip and weather data are present;
    #only performing one test since there is already a comprehensive unit test
    #for download_if_needed, which is the only dependent function that may
    #cause problems
    def testDataPresent(self):
        #1
        result=plot_daily_totals()
        expected_explanation='Daily totals were plotted.'
        self.assertEqual(result, expected_explanation)

if __name__ == '__main__':
    unittest.main()
