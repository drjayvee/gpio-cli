#!/usr/bin/python -tt

import RPi.GPIO as GPIO
import sys

class GPIOCLI:
	def __init__(self, pinId, quiet=False):
		self.pinId = pinId
		if quiet:
			GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(pinId, GPIO.OUT)

	def __del__(self):
		GPIO.cleanup()

	def setOutLow(self):
		GPIO.output(self.pinId, GPIO.LOW)

	def setOutHigh(self):
		GPIO.output(self.pinId, GPIO.HIGH)

def printHelp():
	print """
	GPIO-CLI usage:
		gpiocli.py	cleanup
		gpiocli.py	PinID (HIGH|LOW) [-q]
	"""

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print "Invalid number of arguments"
		printHelp()
		exit(1)

	# handle cleanup
	if sys.argv[1] == "cleanup":
		GPIO.cleanup()
		exit()
	elif len(sys.argv) < 2:
		printHelp()
		exit()

	# set pin id
	gpiocli = GPIOCLI(
		int(sys.argv[1]),							# PinID
		len(sys.argv) == 4 and sys.argv[3] == "-q"  # optional -q flag
	)

	setting = sys.argv[2].lower()
	if setting == "high":
		gpiocli.setOutHigh()
	elif setting == "low":
		gpiocli.setOutLow()
	else:
		print "Invalid setting"
		printHelp()
		exit(1)
