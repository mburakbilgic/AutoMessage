from PIL.ImageOps import grayscale
import pyautogui
import time
import webbrowser
import argparse
from time import sleep

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..','..'))

from wp_batch.wp_message_batch import MessageBatch

class AutoMessage:
    def __init__(self):
        self.image_path = '%s/wp_images/' %os.path.dirname(os.path.realpath(__file__)).replace('\\','/')

    def message_send_wp(self):
        #TODO: input needed for schedule time
        unique_batch = MessageBatch().msg_unique_batch()
        batch = MessageBatch().msg_batch()
        
        open_wp_image_path = '%s/open_whatsapp.png' %self.image_path
        click_sent_image_path = '%s/click_sent.png' %self.image_path

        for _pnumber,_msg in self.batch.items():
            webbrowser.open_new_tab(f'https://api.whatsapp.com/send?phone=+90{_pnumber}&text={_msg}')
            time.sleep(15)

            pyautogui.click(pyautogui.locateCenterOnScreen(open_wp_image_path, grayscale = False))
            time.sleep(15)

            pyautogui.click(pyautogui.locateCenterOnScreen(click_sent_image_path, grayscale = False))
            time.sleep(5)
    
    def run(self):
        self.message_send_wp()

parser = argparse.ArgumentParser()
parser.add_argument('-c',help='Code Runner')
args = parser.parse_args()

if args.c == 'run':
    wp_challenge = AutoMessage()
    wp_challenge.run()