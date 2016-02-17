from plot_x_vs_y import plot_x_vs_y
from pronto_utils import get_trips_and_weather
import os
import unittest


class Plot_x_vs_y_Tester(unittest.TestCase):

    def test_valid_plot(self):
        """
        Here we check that the pdf file is properly generated
        when a valid data frame and columns are supplied as
        arguments to the function.
        """

        # download the trip and weather data
        # NOTE: we turn off alerts about whether or not data
        # has already been downloaded within the pronto_utils.py
        # code in order to make unit test output cleaner
        data = get_trips_and_weather()

        fileName = 'Temp_and_Membership'
        plot_x_vs_y(data,'Mean_Temperature_F','Annual Member', fileName)
        filePath = os.getcwd() + '\\' + fileName + '.pdf'
        self.assertTrue(os.path.exists(filePath))

    def test_invalid_plot_no_file(self):
        """
        Here we check that the pdf file is NOT generated
        when a valid data frame, but an invalid column
        are supplied to the function.
        """

        data = get_trips_and_weather()

        fileName = 'Temp_and_Membership_invalid'
        plot_x_vs_y(data,'Mean_Temperaturezzzz_F','Annual Member', fileName)
        filePath = os.getcwd() + '\\' + fileName + '.pdf'
        self.assertFalse(os.path.exists(filePath))

    def test_invalid_plot_exception_trhown(self):
        """
        Here we check that a TypeError exception is
        thrown when a valid data frame, but an invalid
        column are supplied to the function.
        """

        data = get_trips_and_weather()

        fileName = 'Temp_and_Membership_invalid'
        plot_x_vs_y(data,'Mean_Temperaturezzzz_F','Annual Member', fileName)
        filePath = os.getcwd() + '\\' + fileName + '.pdf'
        #self.assertFalse(os.path.exists(filePath))
        self.assertRaises(KeyError)

if __name__ == '__main__':
    unittest.main()
