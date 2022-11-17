# Import modules

from tkinter import *
from health.bmi import User, Bmicalculator

# Create class for the outer 

class Rahmen(Frame):
    def __init__(self,master=None,labeltext=''):
        Frame.__init__(self, master)

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self, master)

# Close the mainloop for creating window

root=Tk()
app=Application(master=root)
app.mainloop()
