import usb.core
import usb.util
import threading

class USBReaderThread(threading.Thread):
    def __init__(self, device, epAdress, maxInputSize, evtCallback):
        self.device = device
        self.epAdress = epAdress
        self.maxInputSize = maxInputSize
        self.evtCallback = evtCallback

        cfg = self.device.get_active_configuration()
        assert cfg is not None

        ep = usb.util.find_descriptor(cfg, find_all=True, bEndpointAddress=self.epAdress)
        assert ep is not None
        
        threading.Thread.__init__(self)

    def run(self):
        while True:
            data = self.device.read(self.epAdress, self.maxInputSize, 0)
            self.evtCallback(data)

ENDPOINT_HMI_ADRESS = 0x82
ENDPOINT_HMI_MAXSIZEPACKAGE = 0x40

ENDPOINT_MIDI_ADRESS = 0x81
ENDPOINT_MIDI_MAXSIZEPACKAGE = 0x200

class USBReader():

    def __init__(self, vendorId, productId):

        self.device = usb.core.find(idVendor=vendorId, idProduct=productId)
        self.device.set_configuration()

        self.hmi_subscriber = []
        self.midi_key_subscriber = []
        self.midi_control_subscriber = []

        self.cfg = self.device.get_active_configuration()

        hmiReader = USBReaderThread(self.device, ENDPOINT_HMI_ADRESS, ENDPOINT_HMI_MAXSIZEPACKAGE, self.handle_hmi_event)
        midiReader = USBReaderThread(self.device, ENDPOINT_MIDI_ADRESS, ENDPOINT_MIDI_MAXSIZEPACKAGE, self.handle_midi_event)
        self.readerThreads = [hmiReader, midiReader]

        self.wheel = 0
        
    def add_hmi_subscriber(self, subscriber):
        self.hmi_subscriber.append(subscriber)

    def add_midi_key_subscriber(self, subscriber):
        self.midi_key_subscriber.append(subscriber)

    def add_midi_control_subscriber(self, subscriber):
        self.midi_control_subscriber.append(subscriber)

    def handle_midi_event(self, event):
        print(event)
        if(event[1] == 144 or \
           event[1] == 128 or \
           event[1] == 208):
               self.informSubscribers(self.midi_key_subscriber, event)
        else:
               self.informSubscribers(self.midi_control_subscriber, event)

    def start(self):
        for thread in self.readerThreads:
            thread.start()

    def informSubscribers(self, subscriber_list, event):
        if(len(subscriber_list) != 0):
            for sub in subscriber_list:
                    sub.handle_event(event)

    def handle_hmi_event(self, event):
        self.informSubscribers(self.hmi_subscriber, event)

       
