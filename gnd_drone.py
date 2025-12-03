#!/usr/bin/env python

"""
Check CPU Serial Number.
cat /proc/cpuinfo
"""

import socket
import pickle
from time import time, sleep
#from threading import Thread
from dronekit import connect, VehicleMode

chans = []

# UDP IP address and port to listen on
UDP_IP = "0.0.0.0"
UDP_PORT = 5005

sskey = '00000000ca127702'


def mavlink_conn(retries=3, delay=3):
    for i in range(retries):
        try:
            # Create the connection to drone
            print('Connecting to FC')
            #vehicle = connect('tcp:192.168.1.145:5762', rate=40)
            vehicle = connect("/dev/ttyAMA0", baud=57600, wait_ready=True,  timeout=100, rate=40)
        except dronekit.APIException:
            print("Unable to connect to FC!")
            #pass
            sleep(delay)

    print('Connected to FC')

def sinfo():
    global skey
    f = open('/proc/cpuinfo','r')
    for l in f:
        if l.startswith('Serial'):
            skey = l[-18:].strip()

def pwmCalc(crsf_value):
#    pwm = 1500 + (0.625 * (crsf_value - 992))
    pwm = crsf_value * 0.61 + 895
    return int(pwm)

def rcOverrides(ch1, ch2, ch3, ch4, ch5, ch6, ch7, ch8):
    vehicle.channels.overrides = {'1': ch1, '2': ch2, '3': ch3, '4': ch4, '5': ch5, '6': ch6, '7': ch7, '8': ch8}

def openSerial():
    global chans
    mavlink_conn()
    #sinfo()
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
                    #print(pwmCalc(chans[0]), pwmCalc(chans[1]), pwmCalc(chans[2]), pwmCalc(chans[3]), pwmCalc(chans[4]), pwmCalc(chans[5]), pwmCalc(chans[6]), pwmCalc(chans[7]))
                    rcOverrides(pwmCalc(chans[0]), pwmCalc(chans[1]), pwmCalc(chans[2]), pwmCalc(chans[3]), pwmCalc(chans[4]), pwmCalc(chans[5]), pwmCalc(chans[6]), pwmCalc(chans[7]))
                    sleep(0.01)
            except TimeoutError:
                #print("STOP!")
                rcOverrides(1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500)
                pass
    return bytes(chans)

if __name__ == "__main__":
    openSerial()
