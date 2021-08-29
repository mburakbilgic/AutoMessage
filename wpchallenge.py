from PIL.ImageOps import grayscale
import pyautogui
import time
import webbrowser
import argparse
import os
import pandas as pd
from time import sleep

class AutoMessage:
    def __init__(self):
        self.current_path = os.getcwd()
        print(self.current_path)
        self.arr_name = []
        self.arr_pnumber = []
        self.arr_msg = []
        self.batch = {}

    def data(self):
        _data = pd.read_csv("C:/Users/muham/Desktop/wpchallenge/phonebook.csv", sep=',',header=0)
        for idx in _data.index:
            pnumber = _data.loc[idx,'phonenumber']
            name = _data.loc[idx,'name']
            
            self.arr_pnumber.append(str(pnumber))
            self.arr_name.append(name)

    def message_batch(self):
        for idx_name in self.arr_name:
            msg='Hi %s! my new phone number is 5341903034, please remove the other. Thank you!' %idx_name
            self.arr_msg.append(msg)

        self.batch = dict(zip(self.arr_pnumber,self.arr_msg))

    def message_send_wp(self):
        open_wp_image_path = '%s\open_whatsapp.png' %self.current_path
        click_sent_image_path = '%s\click_sent.png' %self.current_path

        for _pnumber,_msg in self.batch.items():
            webbrowser.open_new_tab(f'https://api.whatsapp.com/send?phone=+90{_pnumber}&text={_msg}')
            time.sleep(15)

            pyautogui.click(pyautogui.locateCenterOnScreen(open_wp_image_path, grayscale = False))
            time.sleep(15)

            pyautogui.click(pyautogui.locateCenterOnScreen(click_sent_image_path, grayscale = False) %self.current_path)
            time.sleep(5)
    
    def run(self):
        self.data()
        self.message_batch()
        self.message_send_wp()

parser = argparse.ArgumentParser()
parser.add_argument('-c',help='Code Runner')
args = parser.parse_args()

if args.c == 'run':
    wp_challenge = AutoMessage()
    wp_challenge.run()