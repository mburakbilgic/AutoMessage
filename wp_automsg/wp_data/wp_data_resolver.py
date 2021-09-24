import os
import pandas as pd

class DataResolver:
    def __init__(self):        
        self.data_path = ('%s\phonebook.csv' %os.path.dirname(os.path.realpath(__file__))).replace('\\','/')
        print(self.data_path)
        self.arr_name = []
        self.arr_pnumber = []

    def _data(self):
        
        dataframe = pd.read_csv(self.data_path, sep=',',header=0)

        for idx in dataframe.index:
            pnumber = dataframe.loc[idx,'phonenumber']
            name = dataframe.loc[idx,'name']
            
            self.arr_pnumber.append(str(pnumber))
            self.arr_name.append(name)
        
        return self.arr_pnumber, self.arr_name