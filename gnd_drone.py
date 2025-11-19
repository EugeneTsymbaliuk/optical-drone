#!/usr/bin/env python

"""
Check CPU Serial Number.
cat /proc/cpuinfo
"""

import socket
import pickle
from time import time, sleep
from threading import Thread
from dronekit import connect, VehicleMode

chans = []

# UDP IP address and port to listen on
UDP_IP = "0.0.0.0"
UDP_PORT = 5005

sskey = '00000000ca127702'

# Create the connection to drone
print('Connecting to FC')
#vehicle = connect('tcp:192.168.1.145:5762', rate=40)
vehicle = connect("/dev/ttyAMA0", baud=57600, wait_ready=True,  timeout=100, rate=40)
print('Connected to FC')

def sinfo():
    global skey
    f = open('/proc/cpuinfo','r')
    for l in f:
        if l.startswith('Serial'):
            skey = l[-18:].strip()

def pwmCalc(crsf_value):
#    pwm = 1500 + (0.625 * (crsf_value - 992))
    pwm = crsf_value * 0.61 + 894
    return int(pwm)

def rcOverrides(roll, pitch, thr=1500, yaw=1500, arm=2000):
    vehicle.channels.overrides = {'1': roll, '2': pitch, '3': thr, '4': yaw, '6': arm}

def openSerial():
    global chans
    sinfo()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    sock.settimeout(3.0)
    if skey == skey:
        while True:
            try:
                data, addr = sock.recvfrom(1024)
                chans = pickle.loads(data)
                if chans[0] > 1:
                    #print(chans[0], chans[1])
                    #print(pwmCalc(chans[0]), pwmCalc(chans[1]))
                    rcOverrides(pwmCalc(chans[0]), pwmCalc(chans[1]), arm=pwmCalc(chans[5]))
                    sleep(0.01)
            except TimeoutError:
                print("STOP!")
                rcOverrides(1500, 1500)
                pass
    return bytes(chans)

if __name__ == "__main__":
    Thread(target=openSerial).start()
