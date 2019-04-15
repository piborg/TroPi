#!/usr/bin/env python
# coding: Latin-1

# Import library functions we need
from __future__ import print_function
from tropi import TroPi
import time
import sys

# Settings
delay = 0.02
ledCount = TroPi.MAX_LEDS
steps = 60
seperation = 20

# Setup the TroPi
troPi = TroPi()
troPi.SetAllColours(0,0,0)

# Loop over the sequence until the user presses CTRL+C
print ('Running colourwave demo. Press CTRL+C to finish')
bufferSize = ledCount * seperation
bufferedColours = [[0,0,0] for i in range(bufferSize)]
try:
    while True:
        # Loop over a set of different hues:
        for hue in range(steps * 3):
            # Get hue into the 0 to 3 range
            hue /= float(steps)
            # Decide which two channels we are between
            if hue < 1.0:
                # Red to Green
                red = 1.0 - hue
                green = hue
                blue = 0.0
            elif hue < 2.0:
                # Green to Blue
                red = 0.0
                green = 2.0 - hue
                blue = hue - 1.0
            else:
                # Blue to Red
                red = hue - 2.0
                green = 0.0
                blue = 3.0 - hue
            # Add the next colour into our list and remove the oldest
            bufferedColours.insert(0, [red, green, blue])
            bufferedColours.pop()
            # Set the chosen colours for all LEDs
            ledColours = [bufferedColours[i] for i in range(0, bufferSize, seperation)]
            troPi.SetEachColour(ledColours)
            # Wait a short while
            time.sleep(delay)
except KeyboardInterrupt:
    # User has pressed CTRL+C, clear the LEDs and stop
    troPi.SetAllColours(0,0,0)
    print ('Done')
