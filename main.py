import config
import gui
import config_io
import usb_reader
import midi_router
import midi_event_sender

from threading import Thread

STORAGE_FILENAME = "configuration.sav"

class kontrol_main:
    def __init__(self):

        self.database = {"when_im_alone" : {"name" : {"When I'm Alone"}, "midi_program" : 3}, \
                        "beautiful_day" : {"name" : {"Beautiful Day"}, "midi_program" : 0}, \
                         "im_all_over_it" : {"name" : {"I'm all over it"}, "midi_program" : 2}, \
                         "broken_wings" : {"name" : {"Broken Wings"}, "midi_program" : 1}}

        self.setlist = ["im_all_over_it", "beautiful_day", "broken_wings", "when_im_alone"]

        input_names = ["Komplete Kontrol - 1"]
        output_names = ["midi1"]

        namelist = []

        for so in self.setlist:
            namelist += self.database[so]["name"]
            
        self.controller = gui.instrument_controller(self.setlist, namelist, self)

        self.usb = usb_reader.USBReader(self.controller)
        self.midi_io = midi_router.MidiRouter()

        for i in input_names:
            self.midi_io.add_midi_device(i, "input")

        for o in output_names:
            self.midi_io.add_midi_device(o, "output")
            self.midi_io.activate_midi_key_route(o)
            self.midi_io.activate_midi_control_route(o)

        self.midi_sender = midi_event_sender.MidiEventSender(self.midi_io)

    def start(self):

        self.usb.start()
        #self.midi_io.start()
        #self.controller.start()

    def setActiveInstrument(self, instrument):
        program_id = self.database[instrument]["midi_program"]
        self.midi_sender.set_program_event(program_id)

main = kontrol_main()
main.start()
