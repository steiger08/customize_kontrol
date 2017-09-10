midi_router = MidiRouter()
                        
input_names = ["Komplete Kontrol - 1"]
output_names = ["midi1", "midi2"]

for i in input_names:
    midi_router.add_midi_device(i, "input")

for o in output_names:
    midi_router.add_midi_device(o, "output")
    midi_router.activate_midi_key_route(o)
    midi_router.activate_midi_control_route(o)


midi_router.start()

time.sleep(10)
midi_router.deactivate_midi_key_route("midi1")
midi_router.deactivate_midi_control_route("midi1")
