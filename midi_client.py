#!/usr/bin/env python
import sys
import os
import pygame
import pygame.midi
from pygame.locals import *
import rtmidi


# display a list of MIDI devices connected to the computer
def print_device_info():
    for i in range( pygame.midi.get_count() ):
        r = pygame.midi.get_device_info(i)
        (interf, name, input, output, opened) = r
        in_out = ""
        if input:
            in_out = "(input)"
        if output:
            in_out = "(output)"
        print ("%2i: interface: %s, name: %s, opened: %s %s" %
               (i, interf, name, opened, in_out))
pygame.init()
pygame.fastevent.init()
event_get = pygame.fastevent.get
event_post = pygame.fastevent.post
pygame.midi.init()
print ("Available MIDI devices:")
print_device_info();

# Change this to override use of default input device
device_id = None
if device_id is None:
    input_id = pygame.midi.get_default_input_id()
    output_id1 = 12
    output_id2 = 13
    
else:
    input_id = device_id
print ("Using input_id: %s" % input_id)

i = pygame.midi.Input( input_id )
o1 = pygame.midi.Output( output_id1 )
o2 = pygame.midi.Output( output_id2 )


print ("Logging started:")
going = True
while going:
    events = event_get()
    for e in events:
        if e.type in [QUIT]:
            going = False
        if e.type in [KEYDOWN]:
            going = False
        #if e.type in [pygame.midi.MIDIIN]:
            #print(e)
            # print information to console
    # if there are new data from the MIDI controller
    if i.poll():
        midi_events = i.read(10)
        for midi_event in midi_events:
            if(midi_event[0][0] == 144 or midi_event[0][0] == 128 or midi_event[0][0] == 208): 
                o1.write(midi_events)
                o2.write(midi_events)
            else:
                print(midi_event)
                
