import usb_reader
import hmi_event_interpreter
import midi_router
import time

class HMIEventHandler:
    def wheelButton(self):
        print("Pressed Wheel Button")
    def wheelRight(self):
        print("Wheel Right")
    def wheelLeft(self):
        print("Wheel Left")

class MIDIKeyRouter:
    def __init__(self, midi_output):
        self.midi_output = midi_output

    def handle_event(self, event):
        midi_events = self.translate_usb_key_event_to_midi(event)
        midi_output.send_key_event(midi_events)
        
    def translate_usb_key_event_to_midi(self, usb_key_event):
        #split by 4
        midi_events = []
        print("pre: " + str(usb_key_event))

        while(len(usb_key_event) > 3):
            print(len(usb_key_event))
            l = []
            usb_key_event.pop(0)
            for i in range(3):
                l.append(usb_key_event.pop(0))
            l.append(0)
            midi_events.append(l)

        print("post: " + str(midi_events))
        return midi_events
        
    def split(arr, size):
         arrs = []
         while len(arr) > size:
             pice = arr[:size]
             arrs.append(pice)
             arr   = arr[size:]
         arrs.append(arr)
         return arrs
        
midi_output = midi_router.MidiRouter()
                        
output_names = ["midi1", "midi2"]

for o in output_names:
    midi_output.add_midi_device(o)
    midi_output.activate_midi_key_route(o)
    midi_output.activate_midi_control_route(o)


vendorId = 0x17CC
productId = 0x1410

hmi_evt_hdlr = HMIEventHandler()

hmi_interpreter = hmi_event_interpreter.HMIEventInterpreter(hmi_evt_hdlr)
midi_router1 = MIDIKeyRouter(midi_output)

usb = usb_reader.USBReader(vendorId, productId)
usb.start()
usb.add_hmi_subscriber(hmi_interpreter)
usb.add_midi_key_subscriber(midi_router1)
