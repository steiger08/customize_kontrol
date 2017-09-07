import usb.core
import usb.util

def main():
    device = usb.core.find(idVendor=0x17CC, idProduct=0x1410)
    print(device)
    
##    for cfg in device:
##        print("Konfiguration")
##        print(cfg)
##        for intf in cfg:
##            print("Interfaces")
##            print(str(intf.bInterfaceNumber) + ' , ' + str(intf.bAlternateSetting))
##            for ep in intf:
##                print("Endpoints")
##                print(ep.bEndpointAddress)

    device.set_configuration()

    cfg = device.get_active_configuration()
    assert cfg is not None

    hid = usb.util.find_descriptor(cfg, find_all=True, bInterfaceNumber=2)
    assert hid is not None
    #device.detach_kernel_driver(hid)

    ep = usb.util.find_descriptor(cfg, find_all=True, bEndpointAddress=0x82)
    assert ep is not None

    wheel = 0

    while True:
        try:
            data = device.read(0x82, 0x40, 0)
            print(data)
            if(data[0] == 1):
                if(data[6] != wheel):
                    wheel = data[6]
                    print("wheel moved to position " + str(wheel))
                    
                if(data[2] == 8):
                    print("nav_right button")
                if(data[2] == 32):
                    print("nav_left button")
                if(data[2] == 16):
                    print("nav_down button")
                if(data[2] == 128):
                    print("nav_up button")
                if(data[2] == 64):
                    print("back button")
                if(data[2] == 1):
                    print("stop button")
                if(data[2] == 2):
                    print("rec button")
                if(data[2] == 4):
                    print("play button")
                if(data[1] == 1):
                    print("wheel button")
                if(data[1] == 32):
                    print("instance button")
                if(data[1] == 16):
                    print("browse button")
                if(data[1] == 4):
                    print("enter button")
                if(data[3] == 1):
                    print("shift button")
                if(data[3] == 128):
                    print("ffw button")      
                if(data[3] == 64):
                    print("rwd button") 
                if(data[3] == 8):
                    print("loop button")
            
        except usb.core.USBError as e:
            data = None
            print(e)

if __name__ == '__main__':
  main()
