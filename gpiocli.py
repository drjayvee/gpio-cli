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

	def setOutLow(self):
#		print "Setting", self.pinId, "low"
		GPIO.output(self.pinId, GPIO.LOW)

	def setOutHigh(self):
#		print "Setting", self.pinId, "high"
		GPIO.output(self.pinId, GPIO.HIGH)

def printHelp():
	print """
	GPIO-CLI usage:
		gpiocli.py	cleanup
		gpiocli.py	PinID (HIGH|LOW) [-q]
	"""

if __name__ == '__main__':
	if len(sys.argv) < 1:
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
#	print "pin id", argv[1]
	gpiocli = GPIOCLI(
		int(sys.argv[1]),							# PinID
		len(sys.argv) == 4 and sys.argv[3] == "-q"  # optional -q flag
	)

	if sys.argv[2] == "HIGH":
		gpiocli.setOutHigh()
	elif sys.argv[2] == "LOW":
		gpiocli.setOutLow()
	else:
		print "Invalid setting"
		printHelp()
		exit(1)
