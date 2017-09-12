from tkinter import *

class instrument_view():
    def __init__(self, namelist, controller):

        self.namelist = namelist
        self.controller = controller
        
        self.master = Tk("Instrument Selection")

        listFont = font.Font(family="Calibri",size=24)
        selFont = font.Font(family="Calibri",size=30, weight="bold")

        highcol = "#adc6b1"
        bgcol = "#dae8dc"
        txtbg = "#59685c"
        
        self.listbox = Listbox(self.master, \
                               font = listFont, \
                               activestyle = DOTBOX, \
                               selectborderwidth = 2, \
                               selectbackground = txtbg, \
                               setgrid = 4, \
                               highlightcolor = highcol, \
                               highlightthickness = 3, \
                               bg = bgcol)
        
        for item in self.namelist:
            self.listbox.insert(END, item)

        self.list_size = len(self.namelist)
        self.index = 0

        self.selLabelText = StringVar()

        self.selLabel = Label(self.master, \
                         textvariable = self.selLabelText, \
                         font = selFont)

        self.selLabel.pack()
        self.listbox.pack()

    def run(self):
        self.listbox.selection_set(self.index)
        self.activateCurrent()

        self.master.update()
        self.master.mainloop()

    def changeSelection(self, dif):
        self.listbox.selection_clear(0, END)
        
        self.index += dif

        while(self.index > self.list_size-1):
            self.index -= self.list_size
        while(self.index < 0):
            self.index += self.list_size
            
        self.listbox.select_set(self.index)

    def activateCurrent(self):
        self.selLabelText.set(self.namelist[self.index])
        self.controller.instrumentSelectionChanged(self.index)
        self.master.update()

class instrument_controller:
    def __init__(self, idlist, namelist, event_hdlr):
        self.idlist = idlist
        self.namelist = namelist
        self.event_hdlr = event_hdlr
        self.view = instrument_view(namelist, self)

    def start(self):
        self.view.run()

    def wheelRight(self):
        self.view.changeSelection(1)

    def wheelLeft(self):
        self.view.changeSelection(-1)

    def wheelButton(self):
        self.view.activateCurrent()

    def instrumentSelectionChanged(self, index):
        self.event_hdlr.setActiveInstrument(self.idlist[index])
        
    
