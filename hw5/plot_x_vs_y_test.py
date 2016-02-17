import os
import unittest

from plot_x_vs_y import plot_x_vs_y
from pronto_utils import remove_data
from pronto_utils import get_trips_and_weather


class Test_plot_x_vs_y(unittest.TestCase):


  def testDoesPDFAlreadyExist(self):
    remove_data('plot_x_vs_y.pdf')
    plot_x_vs_y(get_trips_and_weather(),'Annual Member','Min_TemperatureF',
        'plot_x_vs_y')
    result = plot_x_vs_y(get_trips_and_weather(),'Annual Member',
        'Min_TemperatureF','plot_x_vs_y')
    self.assertTrue(result)

  def testWasPDFCreated(self):
      remove_data('plot_x_vs_y.pdf')
      plot_x_vs_y(get_trips_and_weather(),'Annual Member','Min_TemperatureF',
          'plot_x_vs_y')
      self.assertTrue(os.path.exists('plot_x_vs_y.pdf'))

if __name__ == '__main__':
    unittest.main()
