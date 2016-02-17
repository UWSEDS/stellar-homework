'''Units test for download_if_needed.py'''

import unittest
from pronto_utils import download_if_needed
import os

class TestDownload(unittest.TestCase):
    #Test URLs that are correctly inputted
    def testCorrectURLs(self):
        #1
        if os.path.isfile('Fig3-1.xls'):
            os.remove('Fig3-1.xls')
        url='http://www.econ.yale.edu/~shiller/data/Fig3-1.xls'
        filename='Fig3-1.xls'
        result=download_if_needed(url,filename)
        expected_explanation=('Downloading', filename)
        self.assertEqual(result, expected_explanation)
        #2
        if os.path.isfile('dataYale.xls'):
            os.remove('dataYale.xls')
        url='http://www.econ.yale.edu/~shiller/data/ie_data.xls'
        filename='dataYale.xls'
        result=download_if_needed(url,filename)
        expected_explanation=('Downloading', filename)
        self.assertEqual(result, expected_explanation)

    #Test to make sure file will not be redownloaded if it already exists
    def testFileExists(self):
        #1
        url='https://s3.amazonaws.com/pronto-data/open_data_year_one.zip'
        filename='open_data_year_one.zip'
        result=download_if_needed(url,filename)
        expected_explanation=(filename, 'already exists')
        self.assertEqual(result, expected_explanation)

    #Test to make sure function throws an error when incorrect URL is given
    def testIncorrectURLs(self):
        #1
        url='https://geegle.com'
        filename='testFilename.txt'
        result=download_if_needed(url,filename)
        expected_explanation='Could not connect to server. Please check to make sure the URL is valid and try again.'
        self.assertEqual(result, expected_explanation)
        #2
        url='https://s3.amazws.com/pronto-data/open_data_year_one.zip'
        filename='data_year_one.zip'
        result=download_if_needed(url,filename)
        expected_explanation='Could not connect to server. Please check to make sure the URL is valid and try again.'
        self.assertEqual(result, expected_explanation)

    #Test to make sure user is warned if they do not specify a URL
    def testEmptyURL(self):
        #1
        url=''
        filename='testFilename.txt'
        result=download_if_needed(url,filename)
        expected_explanation='No host specified.'
        self.assertEqual(result, expected_explanation)

    #Test to make sure filename is correct    
    def testEmptyFilename(self):
        #1
        url=''
        filename=''
        result=download_if_needed(url,filename)
        expected_explanation='Please input a correct filename.'
        self.assertEqual(result, expected_explanation)
        #2
        url='https://google.com'
        filename=''
        result=download_if_needed(url,filename)
        expected_explanation='Please input a correct filename.'
        self.assertEqual(result, expected_explanation)


if __name__ == '__main__':
    unittest.main()
