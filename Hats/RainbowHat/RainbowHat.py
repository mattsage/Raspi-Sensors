#!/usr/bin/env python

import signal
import rainbowhat
import datetime

timenow = datetime.datetime.now().strftime("%H%M")

def display_message(message):
    rainbowhat.display.print_str(message)
    rainbowhat.display.show()

@rainbowhat.touch.A.press()
def press_a(channel):
    rainbowhat.rainbow.clear()
    display_message("NOAH")
    print ("Button A touched!")
    rainbowhat.rainbow.set_all(255,0,0)
    rainbowhat.rainbow.show()
    rainbowhat.lights.rgb(1,0,0)

@rainbowhat.touch.B.press()
def press_b(channel):
    rainbowhat.rainbow.clear()
    display_message("Jake")
    print ("Button B touched!")
    rainbowhat.rainbow.set_all(0,255,0)
    rainbowhat.rainbow.show()
    rainbowhat.lights.rgb(0,1,0)

@rainbowhat.touch.C.press()
def press_c(channel):
    rainbowhat.rainbow.clear()
    display_message("Matt")
    print ("Button C touched!")
    rainbowhat.rainbow.set_all(0,0,255)
    rainbowhat.rainbow.show()
    rainbowhat.lights.rgb(0,0,1)

	
display_message(timenow)
rainbowhat.lights.rgb(1,1,1)

signal.pause()
