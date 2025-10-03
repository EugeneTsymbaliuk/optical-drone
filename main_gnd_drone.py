
#! /usr/bin/env python

from threading import Thread
from subprocess import call
import gnd_drone
from time import sleep

sleep(20)
Thread(target=gnd_drone.openSerial).start()

