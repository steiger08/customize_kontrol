import midi_router
import time

midi_router1 = midi_router.MidiRouter()
                        
output_names = ["midi1", "midi2"]

for o in output_names:
    midi_router1.add_midi_device(o, "output")
    midi_router1.activate_midi_key_route(o)
    midi_router1.activate_midi_control_route(o)

midi_router1.start()

time.sleep(10)
midi_router1.deactivate_midi_key_route("midi1")
midi_router1.deactivate_midi_control_route("midi1")
