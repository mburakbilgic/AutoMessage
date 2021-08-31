import unittest
import re
from wp_automsg import wp_automsg_script as wpas

class TestEnvrinonment(unittest.TestCase):

    def testData(self):
        expression_1 = len(wpas.AutoMessage()._data)
        expression_2 = wpas.AutoMessage()._data

        self.assertIsNotNone(expression_1,"phonebook.csv should not empty")
        
        pnumber_pattern = r'^5[0-9][0-9][1-9]([0-9]){2}([0-9]){4}$'
        
        for idx in expression_2.index:
            pnumber = expression_2.loc[idx,'phonenumber']
            match = re.search(pnumber_pattern, str(pnumber))
            self.assertIsNotNone(match,"pnumber should be valid")
        
        #TODO:multiple phonenumber
    
    def testInput(self):
        #TODO:input needs to be define
        pass


if __name__ == "__main__":
    unittest.main()