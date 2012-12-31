#!/usr/bin/python -tt

import RPi.GPIO as GPIO
import sys

class GPIOCLI:
    def __init__(self, pinId, cleanUpOnExit=False, verbose=False, quiet=False):
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

    def getOut(self):
        return GPIO.input(self.pinId)

    @staticmethod
    def cleanup():
        GPIO.cleanup()

def printHelp():
    print """
    GPIO cli usage:
        gpiocli.py    cleanup
        gpiocli.py    set PinID (HIGH|LOW) [-c|--cleanup] [-q|--quiet] [-v|--verbose]
        gpiocli.py    get PinID [-c|--cleanup] [-q|--quiet]

    Options:
        -c|--cleanup    Cleanup before exit (settings will be reset)
        -q|--quiet    Suppress GPIO warnings
        -v|--verbose    do tell what's going on (duh)
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
#    elif len(sys.argv) < 3:
#        printHelp()
#        exit()

    # gather parameters
    setting = None
    pinId = int(sys.argv[2])
    if sys.argv[1] == 'set':
        if len(sys.argv) < 3:
            printHelp()
            exit()

        setting = sys.argv[3].lower()
        if not(setting == "high" or setting == "low"):
            print "Invalid setting:", setting
            printHelp()
            exit(1)

        flags = sys.argv[4:]

    else:
        if len(sys.argv) < 2:
            printHelp()
            exit()

        flags = sys.argv[3:]

    cleanUp = False
    verbose = False
    quiet = False
    for flag in flags:
        if flag == "-c" or flag == "--cleanup":
            cleanUp = True
        elif flag == "-q" or flag == "--quiet":
            quiet = True
        elif flag == "-v" or flag == "--verbose":
            verbose = True
        else:
            print "invalid option:", flag
            printHelp()
            exit(1)

    # set up GPIO and set pin
    gpiocli = GPIOCLI(pinId, cleanUp, verbose, quiet)

    if setting is None:
        print "HIGH" if gpiocli.getOut() else "LOW"
    else:
        if setting == "high":
            gpiocli.setOutHigh()
        else:
            gpiocli.setOutLow()
