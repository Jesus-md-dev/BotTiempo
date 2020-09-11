import threading
import time
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.i = 0
        self.sem = threading.Semaphore()
        self.master = master
        self.pack()
        self.create_widgets()

    def fun1(self):
        self.sem.acquire()
        print(self.i)
        self.i = (self.i+1)%2
        print(self.i)
        self.sem.release()
        time.sleep(0.25)

    def fun2(self):
        j = 0
        while j < 10:
            self.sem.acquire()
            print(self.i)
            self.sem.release()
            time.sleep(0.25)
            j+=1

    def create_widgets(self):
        self.Start = tk.Button(self)
        self.Start["text"] = "Start"
        self.Start["command"] = self.fun2
        self.Start.pack(side="left")

        self.Change = tk.Button(self)
        self.Change["text"] = "Change"
        self.Change["command"] = self.fun1
        self.Change.pack(side="right")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()

