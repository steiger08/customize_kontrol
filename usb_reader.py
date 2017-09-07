import usb.core
import usb.util

class USBReader:

    def __init__(self, usb_event_handler):
        self.device = usb.core.find(idVendor=0x17CC, idProduct=0x1410)
        self.device.set_configuration()

        self.cfg = self.device.get_active_configuration()
        assert self.cfg is not None

        self.hid = usb.util.find_descriptor(self.cfg, find_all=True, bInterfaceNumber=2)
        assert self.hid is not None

        self.ep = usb.util.find_descriptor(self.cfg, find_all=True, bEndpointAddress=0x82)
        assert self.ep is not None

        self.wheel = 0
        self.evt_hdlr = usb_event_handler
        
    def run(self):
        while True:
            try:
                data = self.device.read(0x82, 0x40, 0)
                if(data[0] == 1):
                    if(data[6] != self.wheel):
                        if(data[6] > self.wheel):
                            self.evt_hdlr.wheelRight()
                        else:
                            self.evt_hdlr.wheelLeft()
                        self.wheel = data[6]
##                    if(data[2] == 8):
##                        print("nav_right button")
##                    if(data[2] == 32):
##                        print("nav_left button")
##                    if(data[2] == 16):
##                        print("nav_down button")
##                    if(data[2] == 128):
##                        print("nav_up button")
##                    if(data[2] == 64):
##                        print("back button")
##                    if(data[2] == 1):
##                        print("stop button")
##                    if(data[2] == 2):
##                        print("rec button")
##                    if(data[2] == 4):
##                        print("play button")
##                    if(data[1] == 1):
##                        print("wheel button")
##                    if(data[1] == 32):
##                        print("instance button")
##                    if(data[1] == 16):
##                        print("browse button")
##                    if(data[1] == 4):
##                        print("enter button")
##                    if(data[3] == 1):
##                        print("shift button")
##                    if(data[3] == 128):
##                        print("ffw button")      
##                    if(data[3] == 64):
##                        print("rwd button") 
##                    if(data[3] == 8):
##                        print("loop button")
                
            except usb.core.USBError as e:
                data = None
                print(e)

