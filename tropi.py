#!/usr/bin/env python

# Import the library functions we need
from __future__ import print_function
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

class TroPi:
	# Constants
	PIN_CLOCK = 23
	PIN_DATA = 24
	MAX_LEDS = 5

	def __init__(self):
		# Disable warnings
		GPIO.setwarnings(False)
		# Setup the GPIO pins
		GPIO.setup(self.PIN_CLOCK, GPIO.OUT)
		GPIO.setup(self.PIN_DATA, GPIO.OUT)
		# Make sure GPIO pins start in the right state	
		GPIO.output(self.PIN_CLOCK, GPIO.LOW)
		GPIO.output(self.PIN_DATA, GPIO.HIGH)
		# Set initial values
		self.currentColours = [(0, 0, 0) for i in range(self.MAX_LEDS)]

	def WriteByte(self, data):
		# Parse each bit in the byte, MSB first
		for i in range(7, -1, -1):
			# Toggle the clock line
			GPIO.output(self.PIN_CLOCK, GPIO.HIGH)
			# Get just this one bit alone
			maskedBit = (1 << i) & data
			if maskedBit == 0:
				# Bit is low, send low pulse
				GPIO.output(self.PIN_DATA, GPIO.HIGH)
			else:
				# Bit is high, send high pulse
				GPIO.output(self.PIN_DATA, GPIO.LOW)
			# Toggle the clock line
			GPIO.output(self.PIN_CLOCK, GPIO.LOW)
	
	def WriteNewColours(self):
		# Write the initial frame
		for i in range(4):
			self.WriteByte(0)
		# Write the stored values to the LEDs
		for r, g, b in self.currentColours:
			self.WriteByte(0xFF)
			self.WriteByte(int(b * 255))
			self.WriteByte(int(g * 255))
			self.WriteByte(int(r * 255))
		# Write the final frame
		for i in range(4):
			self.WriteByte(0)
		# Final clock toggles
		for i in range(4):
			GPIO.output(self.PIN_CLOCK, GPIO.HIGH)
			GPIO.output(self.PIN_CLOCK, GPIO.LOW)
	
	def SetEachColour(self, colours):
		# Check if we have too many colours
		numValues = len(colours)
		if numValues > self.MAX_LEDS:
			print ('TroPi: %d values given, using first %d only' % (numValues, self.MAX_LEDS))
			numValues = self.MAX_LEDS
		# Overwrite the values stored
		for i in range(numValues):
			colour = colours[i]
			if len(colour) == 3:
				r = colour[0]
				g = colour[1]
				b = colour[2]
				self.currentColours[i] = (r, g, b)
			else:
				print ('TroPi: Colour %d was', colour, ' but we expect an RGB tuple, e.g. (0.5, 0.0, 0.7)')
		# Send the colours to the LEDs
		self.WriteNewColours()

	def SetAllColours(self, red, green, blue):
		# Build our colour tuple
		colour = (red, green, blue)
		# Overwrite the values stored
		for i in range(self.MAX_LEDS):
			self.currentColours[i] = colour
		# Send the colours to the LEDs
		self.WriteNewColours()

	def SetSingleColour(self, ledNumber, red, green, blue):
		# Check if our LED choice is in range
		if (ledNumber < 0) or (ledNumber >= self.MAX_LEDS):
			print ('TroPi: LED number out of range, valid values are 0 to %d' % (self.MAX_LEDS - 1))
		else:
			# Build our colour tuple
			colour = (red, green, blue)
			# Overwrite the value stored
			self.currentColours[ledNumber] = colour
			# Send the colours to the LEDs
			self.WriteNewColours()