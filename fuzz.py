from tropi import TroPi
import time

tropi = TroPi()

red = (1.0, 0.0, 0.0)
blue = (0.0, 0.0, 1.0)

try:
    while True:
        tropi.SetEachColour((red,blue,red,blue,red))
        time.sleep(1)
        tropi.SetEachColour((blue,red,blue,red,blue))
        time.sleep(1)
except KeyboardInterrupt:
    # User has pressed CTRL+C, clear the LEDs and stop
    tropi.SetAllColours(0.0, 0.0, 0.0)
