from tkinter import *

class instrument_view:
    def __init__(self, config):
        self.config = config

    def setup(self):
        self.master = Tk()

        self.helv36 = font.Font(family="Helvetica",size=36, weight="bold")

        self.listbox = Listbox(self.master, font = self.helv36)
        
        #initialize listbox
        for item in self.config.data():
            self.listbox.insert(END, item)

        self.listbox_size = len(self.config.data())
        self.listbox_index = 0
        self.listbox.selection_set(self.listbox_index)

        self.listbox.pack()
        self.master.update()

    def changeSelection(self, dif):

        self.listbox.selection_clear(0, END)
        
        self.listbox_index += dif

        while(self.listbox_index > self.listbox_size-1):
            self.listbox_index -= self.listbox_size
        while(self.listbox_index < 0):
            self.listbox_index += self.listbox_size

        self.listbox.selection_set(self.listbox_index)
        self.master.update()

class instrument_controller:
    def __init__(self, view):
        self.view = view

    def wheelRight(self):
        self.view.changeSelection(1)

    def wheelLeft(self):
        self.view.changeSelection(-1)
    
