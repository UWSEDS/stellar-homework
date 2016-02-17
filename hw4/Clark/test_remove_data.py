'''Units test for remove_data.py'''

import unittest
from pronto_utils import remove_data
import os
import shutil

class TestRemoveData(unittest.TestCase):
    #Test to check that cache gets deleted
    def testCache(self):
        #1
        if not os.path.isdir('__pycache__'):
            os.makedirs('__pycache__')
        result=remove_data()
        expected_explanation='Cache and/or .zip folder successfully deleted.'
        self.assertEqual(result, expected_explanation)

    #Test that function works with nothing to delete
    def testNoCache(self):
        #1
        if os.path.isdir('__pycache__'):
            shutil.rmtree('__pycache__')
        result=remove_data()
        expected_explanation='No cache or .zip folder detected.'
        self.assertEqual(result, expected_explanation)


if __name__ == '__main__':
    unittest.main()
