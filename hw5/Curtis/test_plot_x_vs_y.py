''' Unit tests for prime.py '''

import unittest
import wget
import urllib
import pandas as pd
from plot_x_vs_y import plot_x_vs_y, remove_data

class Testplotxvsy(unittest.TestCase):

    # Test whether the file was downloaded
    def testPlotSuccessful(self):
        # 1
        remove_data("fakeplot.png")
        data = pd.read_csv("fake_data.csv")
        result = plot_x_vs_y(data, "fakex", "fakey", "fakeplot.png")
        self.assertTrue(result[0])

    def testBadFileName(self):
        # 1
        data = pd.read_csv("fake_data.csv")
        result = plot_x_vs_y(data, "fakex", "fakey", "fakeplot.pn")
        self.assertFalse(result[1])

    def testGoodFileName(self):
        # 1
        data = pd.read_csv("fake_data.csv")
        result = plot_x_vs_y(data, "fakex", "fakey", "fakeplot.png")
        self.assertTrue(result[1])

    def testAlreadyExists(self):
        # 1
        data = pd.read_csv("fake_data.csv")
        data = pd.read_csv("fake_data.csv")
        result = plot_x_vs_y(data, "fakex", "fakey", "fakeplot.png")
        self.assertTrue(result[2])

    def testNewPlot(self):
        # 1
        remove_data("fakeplot.png")
        data = pd.read_csv("fake_data.csv")
        result = plot_x_vs_y(data, "fakex", "fakey", "fakeplot.png")
        self.assertFalse(result[2])

if __name__ == '__main__':
    unittest.main()
