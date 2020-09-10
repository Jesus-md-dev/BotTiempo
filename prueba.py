import datetime
import time
import winsound
import os
from tkinter import *

class Application(Frame):
    def say_hi(self):
        print ("hi there, everyone!")
    
    def timer(self):
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

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "black"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.evenh = Button(self)
        self.evenh["text"] = "Even Hour",
        self.QUIT["fg"]   = "red"
        self.evenh["command"] = self.evenh

        self.evenh.pack({"side": "left"})

        self.oddh = Button(self)
        self.oddh["text"] = "Odd Hour",
        self.QUIT["fg"]   = "red"
        self.oddh["command"] = self.oddh

        self.oddh.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()