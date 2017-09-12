import midi_event_sender

midi_output = midi_router.MidiRouter()
                        
output_names = ["midi1", "midi2"]

for o in output_names:
    midi_output.add_midi_device(o, "output")
    midi_output.activate_midi_key_route(o)
    midi_output.activate_midi_control_route(o)

event_sender = MidiEventSender(midi_output)

while True:
    event_sender.set_program_event(0)
    time.sleep(3)
    event_sender.set_program_event(1)
    time.sleep(3)
