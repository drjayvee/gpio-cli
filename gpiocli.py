#!/usr/bin/python -tt

import RPi.GPIO as GPIO
import sys

class GPIOCLI:
	def __init__(self, pinId, cleanUpOnExit=True, verbose=False, quiet=False):
		self.pinId = pinId
		self.cleanUp = cleanUpOnExit
		self.verbose = verbose
		if quiet:
			GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(pinId, GPIO.OUT)

	def __del__(self):
		if self.cleanUp:
			if self.verbose:
				print "  GPIO cleanup"
			GPIOCLI.cleanup()

	def setOutLow(self):
		if self.verbose:
			print "  GPIO set {pinId} LOW".format(pinId=pinId)
		GPIO.output(self.pinId, GPIO.LOW)

	def setOutHigh(self):
		if self.verbose:
			print "  GPIO set {pinId} HIGH".format(pinId=pinId)
		GPIO.output(self.pinId, GPIO.HIGH)

	@staticmethod
	def cleanup():
		GPIO.cleanup()

def printHelp():
	print """
	GPIO-CLI usage:
		gpiocli.py	cleanup
		gpiocli.py	PinID (HIGH|LOW) [-n|--no-cleanup] [-q|--quiet] [-v|--verbose]
	"""

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print "Invalid number of arguments"
		printHelp()
		exit(1)

	# handle cleanup
	if sys.argv[1] == "cleanup":
		GPIOCLI.cleanup()
		exit()
	elif len(sys.argv) < 2:
		printHelp()
		exit()

	# gather parameters
	pinId = int(sys.argv[1])
	setting = sys.argv[2].lower()
	if not(setting == "high" or setting == "low"):
		print "Invalid setting:", setting
		printHelp()
		exit(1)

	cleanUp = True
	verbose = False
	quiet = False
	for arg in sys.argv[3:]:
		if arg == "-n" or arg == "--no-cleanup":
			cleanUp = False
		elif arg == "-q" or arg == "--quiet":
			quiet = True
		elif arg == "-v" or arg == "--verbose":
			verbose = True
		else:
			print "invalid option:", arg
			printHelp()
			exit(1)

	# set up GPIO and set pin
	gpiocli = GPIOCLI(pinId, cleanUp, verbose, quiet)

	if setting == "high":
		gpiocli.setOutHigh()
	else:
		gpiocli.setOutLow()
