#!/usr/bin/python
#-*- coding:utf-8 -*-


from tkinter import *
from tkinter.ttk import *
class Select(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.label = Label(self, text="选择项目")
        self.listBox = Listbox(self, height=1)
        self.button = Button(self, text='V', command=self.triggle)
        self.hideList = True
        for i in range(10):
            self.listBox.insert(i, 'Item%d'%i)
            
        self.cmbEditComboList = ['Line1','Line2',]
        self.cmbEditCombo = Combobox(values=self.cmbEditComboList)
        self.cmbEditCombo.grid(row=0, column=4, sticky=N)
        self.label.grid(row=0, column=0, sticky=N)
        self.listBox.grid(row=0, column=1, sticky=N)
        self.button.grid(row=0, column=2, sticky=N)
        self.grid()
    def triggle(self):
        self.hideList ^= 1
        self.listBox.config(height=[self.listBox.size(), 1][self.hideList])
app = Select()
app.mainloop()



























































