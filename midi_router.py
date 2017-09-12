#!/usr/bin/env python
import sys
import os
import pygame
import pygame.midi
from pygame.locals import *
import rtmidi
import threading
import time

class MidiRouter(threading.Thread):
    def __init__(self):
        
        pygame.init()
        pygame.fastevent.init()
        self.event_get = pygame.fastevent.get
        self.event_post = pygame.fastevent.post
        pygame.midi.init()

        self.outputs = {}
        self.active_key_outputs = {}
        self.active_control_outputs = {}

        threading.Thread.__init__(self)
        self.print_device_info()

    def add_midi_device(self, name):
        device = None
        for i in range( pygame.midi.get_count() ):
            info = pygame.midi.get_device_info(i)
            (dev_interface, dev_name, dev_is_input, dev_is_output, dev_opened) = info
            if(str(dev_name) == str("b'" + name + "'") and dev_is_output):
                 device = pygame.midi.Output( i )
                 self.outputs[name] = device
        assert device is not None

    def activate_midi_key_route(self, name):
        self.set_status_midi_route(name, True, True)
        
    def deactivate_midi_key_route(self, name):
        self.set_status_midi_route(name, False, True)

    def activate_midi_control_route(self, name):
        self.set_status_midi_route(name, True, False)
        
    def deactivate_midi_control_route(self, name):
        self.set_status_midi_route(name, False, False)        

    def set_status_midi_route(self, name, status, key_or_control):
        if(key_or_control):
            kc_string = "key"
        else:
            kc_string = "control"        

        print("Set " + kc_string + " of output " + name + " to " + str(status))

        if(key_or_control):
            if(status):
                self.active_key_outputs[name] = self.outputs[name]
            else:
                del self.active_key_outputs[name]
        else:
            if(status):
                self.active_control_outputs[name] = self.outputs[name]
            else:
                del self.active_control_outputs[name]

    # display a list of MIDI devices connected to the computer
    def print_device_info(self):
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

    def send_control_event(self, midi_event):
        for key, o in self.active_control_outputs.items():
            o.write([midi_event])
            
    def send_key_event(self, midi_event):
        for key, o in self.active_key_outputs.items():
            o.write([midi_event])




    
