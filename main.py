# Import modules

from tkinter import *
from health.bmi import User, Bmicalculator

# Create class for the outer frame and entry field

class Rahmen(Frame):
    def __init__(self,master=None,labeltext=''):
        Frame.__init__(self, master)
        self.pack()
        self.label=Label(self,anchor=W,text=labeltext,width=30)
        self.label.pack(side='left')
        self.text=StringVar()
        self.entry=Entry(self,width=30,textvariable=self.text)
        self.entry.pack(side='right')

# Create application frame, input fields and submit/cancel buttons
class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self, master)

# Close the mainloop for creating window

root=Tk()
app=Application(master=root)
app.mainloop()
