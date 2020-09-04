from tkinter import *
import datetime
import time
import winsound
import os


while True:
        abierto = False
        time.sleep(1)
        current_time = datetime.datetime.now()
        if(current_time.hour%2 != 0 and current_time.minute == 55 and abierto == False):
            os.startfile(r"C:\Users\black\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Steam\Nostale.url")
            abierto = True
            time.sleep(59)
        elif(abierto):
            abierto = False