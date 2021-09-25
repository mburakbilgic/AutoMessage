import unittest
import re
import argparse

from wp_automsg.wp_data.wp_data_resolver import DataResolver
from wp_automsg.wp_batch.wp_message_batch import MessageBatch

class TestEnvrinonment(unittest.TestCase):

    def testData(self):
        expression_2,expression_3 = DataResolver()._data()

        pnumber_pattern = r'^5[0-9][0-9][1-9]([0-9]){2}([0-9]){4}$' 

        for idx in expression_2: 
            match = re.search(pnumber_pattern, str(idx))
            self.assertIsNotNone(match,"pnumber should be valid")
        
        self.assertIsNotNone(expression_3,"contact name should be valid")
    
    def run(self):
        self.testData()

parser = argparse.ArgumentParser()
parser.add_argument('-t',help='Test')
args = parser.parse_args()

if args.t == 'test':
    unit_test = TestEnvrinonment()
    unit_test.run()