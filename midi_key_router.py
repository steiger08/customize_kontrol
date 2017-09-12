class MIDIKeyRouter:
    def __init__(self, midi_output):
        self.midi_output = midi_output

    def handle_event(self, event):
        midi_events = self.translate_usb_key_event_to_midi(event)
        self.midi_output.send_key_event(midi_events)
        
    def translate_usb_key_event_to_midi(self, usb_key_event):
        #split by 4
        midi_events = []

        while(len(usb_key_event) > 3):
            outer = []
            inner = []
            usb_key_event.pop(0)
            for i in range(3):
                inner.append(usb_key_event.pop(0))
            inner.append(0)
            outer.append(inner)
            outer.append(0)
            midi_events.append(outer)

        return midi_events

