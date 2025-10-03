#! /usr/bin/env python

from threading import Thread
import gnd_drone

Thread(target=gnd_drone.openSerial).start()

