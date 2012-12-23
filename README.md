# GPIO-cli

## About
Many RaspberryPi users ask how to use GPIO without being root.

The short answer is that that's not possible.

The slightly longer answer is that GPIO really needs to be run as root.
But that doesn't mean your whole python program needs to be run as root. This python module provides a command line interface (CLI) to GPI, so you can call it from shell, like so:

## Using GPIO from shell
```
# Set pin 13 to HIGH, then LOw
sudo python gpiocli.py 13 HIGH
sudo python gpiocli.py 13 LOW
sudo python gpiocli.py cleanup
```

## Using it from python

    import subprocess
    subprocess.check_call(["sudo", "python", "gpiocli.py", "13", "HIGH"])

## Why use sudo?
It's tempting to [use setuid](http://www.tuxation.com/setuid-on-shell-scripts.html) to make the module executable and run as root.
However, that [doesn't work](http://stackoverflow.com/a/8314858)!

## Make script executable
Since the module starts with `#!/usr/bin/python`, you can `chmod +x` this script, and then run
```
sudo ./gpiocli.py 13 HIGH
```
