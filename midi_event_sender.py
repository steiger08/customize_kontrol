import midi_router
import time

class MidiEventSender:
    def __init__(self, midi_receiver):
        self.midi_receiver = midi_receiver

    def set_program_event(self, program_value):
        print("Setting program to ", program_value)

        event = [[192, program_value, 0, 0], 0]

        self.midi_receiver.send_control_event(event)
