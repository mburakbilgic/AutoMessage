import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..','..'))

from wp_automsg.wp_data.wp_data_resolver import DataResolver

class MessageBatch:
    def __init__(self):
        self.batch = {}
        self.unique_batch = {}
    
    def msg_unique_batch(self):
        arr_pnumber,arr_name = DataResolver()._data()
        arr_unique_msg = []

        try:
            desired_name = []
            while True:
                desired_name.append(input('Please enter name: '))
        except KeyboardInterrupt:
            for idx_sname in arr_name:
                if idx_sname in desired_name:
                    uq_msg='Good morning %s! remember today at 9.00 AM we have a meet.' %idx_sname
                    arr_unique_msg.append(uq_msg)

            self.unique_batch = dict(zip(arr_pnumber,arr_unique_msg))
        
        return self.unique_batch

    def msg_batch(self):
        arr_msg = []

        arr_pnumber,arr_name = DataResolver()._data()

        for idx_name in arr_name:
            msg='Hi %s! my new phone number is 5341903034, please remove the other. Thank you!' %idx_name
            arr_msg.append(msg)

        self.batch = dict(zip(arr_pnumber,arr_msg))

        return self.batch