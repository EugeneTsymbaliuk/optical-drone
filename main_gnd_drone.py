#! /usr/bin/env python

import gnd_drone
from threading import Thread

Thread(target=gnd_drone.vehicleState).start()
gnd_drone.openSerial()

