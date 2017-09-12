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
        midi_output.send_key_event([event])
        
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
