#!/usr/bin/env python
#Import the functions we need
from __future__ import print_function
from __future__ import unicode_literals
from tropi import TroPi
import time
import sys
try:
    import urllib.request as urllib
except ImportError:
    import urllib2 as urllib
    
# Setup parameters
# Cheerlights URL to get latest colour from
cheerlightsUrl = 'http://api.thingspeak.com/channels/1417/field/1/last.txt'
# Cheerlights colour map to give over to Tropi
#            Name           Red     Green   Blue
colourMap = {'red':         (1.0,   0.0,    0.0),
             'green':       (0.0,   0.5,    0.0),
             'blue':        (0.0,   0.0,    1.0),
             'cyan':        (0.0,   1.0,    1.0),
             'white':       (1.0,   1.0,    1.0),
             'warmwhite':   (1.0,   1.0,    0.9),
             'purple':      (0.5,   0.0,    0.5),
             'magenta':     (1.0,   0.0,    1.0),
             'yellow':      (1.0,   1.0,    0.0),
             'orange':      (1.0,   0.65,   0.0),
             'pink':        (1.0,   0.75,   0.8),
             'oldlace':     (1.0,   1.0,    0.9)}

#Initialise the TroPi and set all lights to off.
tropi = TroPi()
tropi.SetAllColours(0.0, 0.0, 0.0)
try:
    #Try to run this loop until CTRL+C...
    print('Running Cheerlights demo. Press CTRL+C to finish.')
    while True:
        # Get the cheerlights status from the cheerlights URL.
        cheerlights = urllib.urlopen(cheerlightsUrl)
        colourName = (cheerlights.read()).decode('utf-8')
        cheerlights.close()
        if(colourName in colourMap):
            #If the colour exists, get the colour map from the key.
            red, green, blue = colourMap[colourName]
        else:
            #Print error because colour doesn't exist in the key.
            print('Unexpected colour "', colourName, '"')
            red, green, blue = (0.0, 0.0, 0.0)
        #Set the TroPi colour according to red, green, blue values.
        tropi.SetAllColours(red, green, blue)
        time.sleep(1)
except KeyboardInterrupt:
    # User has pressed CTRL+C, clear the LEDs and stop
    tropi.SetAllColours(0.0, 0.0, 0.0)
