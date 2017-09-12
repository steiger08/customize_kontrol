import usb_reader
import hmi_event_interpreter

class HMIEventHandler:
    def wheelButton(self):
        print("Pressed Wheel Button")
    def wheelRight(self):
        print("Wheel Right")
    def wheelLeft(self):
        print("Wheel Left")

vendorId = 0x17CC
productId = 0x1410

hmi_evt_hdlr = HMIEventHandler()
hmi_interpreter = hmi_event_interpreter.HMIEventInterpreter(hmi_evt_hdlr)

usb = usb_reader.USBReader(vendorId, productId)
usb.start()
usb.add_hmi_subscriber(hmi_interpreter)
