#!/usr/bin/env python
from tropi import TroPi

TroPi = TroPi()

try:
    while True:
        try:
            # Try to get a light value for turning on
            light = int(input("Which light should I turn on? "))
        except ValueError or NameError:
            # Error, we've got something that's not a number.
            print("Expected a number between 0 and 4.")
        else:
            # Set single light on TroPi to white.
            TroPi.SetAllColours(0,0,0)
            TroPi.SetSingleColour(light, 0.3, 0.3, 0.3)
            
except KeyboardInterrupt:
    # User has pressed CTRL+C, clear the LEDs and stop
    TroPi.SetAllColours(0,0,0)
