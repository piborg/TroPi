![PiBorg's TroPi](tropi_banner.png)

Getting Started: [https://www.piborg.org/blog/tropi-getting-started](https://www.piborg.org/blog/tropi-getting-started)

Shop: [https://www.piborg.org/tropi](https://www.piborg.org/tropi)

The TroPi adds a row of 5 programmable LEDs to your Raspberry Pi projects and you can also build you very own light up Trophy display using the additional Trophy kit.

Here you'll find the [driver code](https://github.com/piborg/TroPi/blob/master/tropi.py), and a handful of examples to get you started.

## Installation
Follow the [Getting Started Guide](https://www.piborg.org/blog/tropi-getting-started) for physical installation of the board, then use `git clone https://github.com/piborg/tropi` to clone the TroPi repository locally and use the class within your projects. This will also give you this README and the example scripts showing how to use the TroPi class.

## Examples
There are three examples available in this repository:
* `cheerlights.py` - Runs [Cheerlights](https://cheerlights.com/) on the TroPi. Try running this script using `python cheerlights.py` then Tweet using the #Cheerlights hash tag and a colour eg. Tweeting "#Cheerlights Red" will change the TroPi lights to Red.
* `colourwave.py` - Smoothly changes colours of the TroPi LEDs through the rainbow of colours in a wave from the first LED to the last.
* `whichlight.py` - Asks the user "which light would you like to turn on?". Give a number from 0 to 4 and watch the light come on.

## API

There are a few useful callable functions inside the TroPi class:

* `SetEachColour(colours)` - Provide a list of colours to set each light, see thefuzz.py for an example of usage.
* `SetAllColours(red, green, blue)` - Set all LEDs to the given RGB value eg. `SetAllColours(1.0, 0.0, 0.0)` would set all the lights to red.
* `SetSingleColour(ledNumber, red, green, blue)` - Set a given LED to a colour eg. `SetSingleColour(2, 1.0, 0.0, 0.0)` would set the middle LED to red.

## Further Help
Head over to the [PiBorg Forum](https://forum.piborg.org/forum) and ask for questions if you need further help.
