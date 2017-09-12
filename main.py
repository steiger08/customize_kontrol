import config
import gui
import config_io
import usb_reader
import midi_output
import midi_event_sender
import midi_key_router
import hmi_event_interpreter

from threading import Thread

STORAGE_FILENAME = "configuration.sav"

DEVICE_VENDOR_ID = 0x17CC
DEVICE_PRODUCT_ID = 0x1410

class kontrol_main:
    def __init__(self):

        self.database = {"when_im_alone" : {"name" : {"When I'm Alone"}, "midi_program" : 3}, \
                        "beautiful_day" : {"name" : {"Beautiful Day"}, "midi_program" : 0}, \
                         "im_all_over_it" : {"name" : {"I'm all over it"}, "midi_program" : 2}, \
                         "broken_wings" : {"name" : {"Broken Wings"}, "midi_program" : 1}, \
                         "story" : {"name" : {"Story"}, "midi_program" : 4, "add_sound" : {"midi2"}}}


        self.setlist = ["story", "beautiful_day", "broken_wings", "when_im_alone", "im_all_over_it"]


        namelist = []

        for so in self.setlist:
            namelist += self.database[so]["name"]
            
        self.controller = gui.instrument_controller(self.setlist, namelist, self)


        self.usb = usb_reader.USBReader(DEVICE_VENDOR_ID, DEVICE_PRODUCT_ID)
        self.midi_out = midi_output.MidiRouter()

        midi_router = midi_key_router.MIDIKeyRouter(self.midi_out)
        hmi_interpreter = hmi_event_interpreter.HMIEventInterpreter(self.controller)

        self.usb.add_midi_key_subscriber(midi_router)
        self.usb.add_hmi_subscriber(hmi_interpreter)



        self.midi_out.add_midi_device("midi1")
        self.midi_out.add_midi_device("midi2")
        
        self.midi_out.activate_midi_key_route("midi1")
        self.midi_out.activate_midi_control_route("midi1")

        self.midi_sender = midi_event_sender.MidiEventSender(self.midi_out)

    def start(self):

        self.usb.start()
        self.controller.start()

    def setActiveInstrument(self, instrument):
        program_id = self.database[instrument]["midi_program"]

        self.midi_sender.set_pedal_off()
        self.midi_sender.set_program_event(program_id)

        if("add_sound" in self.database[instrument].keys()):
            self.midi_out.activate_midi_key_route("midi2")
        else:
            self.midi_out.deactivate_midi_key_route("midi2")

main = kontrol_main()
main.start()
