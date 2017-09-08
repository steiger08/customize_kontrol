import config
import gui
import config_io
import usb_reader

from threading import Thread

STORAGE_FILENAME = "configuration.sav"

class kontrol_main:
    def __init__(self):

        self.database = {"when_im_alone" : {"name" : {"When I'm Alone"}, "control_sound" : 1}, \
                        "beautiful_day" : {"name" : {"Beautiful Day"}, "control_sound" : 2}}

        self.setlist = ["when_im_alone", "beautiful_day"]

        namelist = []

        for so in self.setlist:
            namelist += self.database[so]["name"]
            
        controller = gui.instrument_controller(self.setlist, namelist, self)

        usb = usb_reader.USBReader(controller)

        usb.start()
        controller.start()
        
    def setActiveInstrument(self, instrumentId):
        print(instrumentId)

kontrol_main()
