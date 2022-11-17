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
        self.pack()
        self.nameFrame=Rahmen(master,'Name:')
        self.heigtFrame=Rahmen(master,'Körpergröße:')
        self.weightFrame=Rahmen(master,'Gewicht:')
        self.buttonFrame=Frame(master)
        self.buttonFrame.pack()
        self.okButton=Button(
            self.buttonFrame,text='OK',width=20)
        self.okButton['command']=self.action
        self.okButton.pack(side='left')
        self.cancelButton=Button(
            self.buttonFrame,text='Abbrechen',width=20,command=root.destroy)
        self.cancelButton.pack(side='right')
        self.listbox=Listbox(master)
        self.listbox.pack(fill=BOTH)
    def action(self):
        user=User(
            self.nameFrame.text.get(),
            self.heightFrame.text.get())
        bmirechner=Bmicalculator()
        bmi=bmirechner.calculate(
            user.height,
            self.weightFrame.text.get())
        bmirechner.add(user.name,bmi)
        self.listbox.delete(0,END)
        if user.name in bmirechner.datastorage:
            bmis=bmirechner.datastorage[user.name]
            for bmi in bmis:
                self.listbox.insert(
                    END,
                    user.name+':'+
                    str(bmi)+':'+
                    bmirechner.evaluate(bmi))

# Close the mainloop for creating window

root=Tk()
app=Application(master=root)
app.mainloop()
