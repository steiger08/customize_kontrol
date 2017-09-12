import usb_reader
import hmi_event_interpreter
import midi_router
import time
import midi_key_router

class HMIEventHandler:
    def wheelButton(self):
        print("Pressed Wheel Button")
    def wheelRight(self):
        print("Wheel Right")
    def wheelLeft(self):
        print("Wheel Left")

        
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
midi_router1 = midi_key_router.MIDIKeyRouter(midi_output)

usb = usb_reader.USBReader(vendorId, productId)
usb.start()
usb.add_hmi_subscriber(hmi_interpreter)
usb.add_midi_key_subscriber(midi_router1)
