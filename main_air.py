#! /usr/bin/env python

from subprocess import call
from threading import Thread

import fly_by_ip_air
from time import sleep

sleep(10)
Thread(target=fly_by_ip_air.openSerial).start()

