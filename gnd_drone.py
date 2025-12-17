#!/usr/bin/env python

"""
Check CPU Serial Number.
cat /proc/cpuinfo
"""

import os
import socket
import pickle
from time import time, sleep
import dronekit
from dronekit import connect, VehicleMode

chans = []

# UDP IP address and port to listen on
UDP_IP = "0.0.0.0"
UDP_PORT = 5005

sskey = '00000000ca127702'
# Files dir
files_dir = os.path.expanduser("~/files/")

for i in range(3):
    try:
        # Create the connection to drone
        print('Connecting to FC')
        vehicle = connect("/dev/ttyAMA0", baud=57600, wait_ready=True,  timeout=100, rate=40)
    except dronekit.APIException:
        print("Unable to connect to FC!")
        sleep(1)

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

def vehicleState():
    global vehicle
    while True:
        with open(files_dir + 'sats.txt', 'r+') as s, open(files_dir + 'volts.txt', 'r+') as v, open(files_dir + 'amps.txt', 'r+') as c, open(files_dir + 'heading.txt', 'r+') as h, open(files_dir + 'gspeed.txt', 'r+') as gs, open(files_dir + 'arm.txt', 'r+') as  arm, open(files_dir + 'lat.txt', 'r+') as lat, open(files_dir + 'lon.txt', 'r+') as lon, open(files_dir + 'alt.txt', 'r+') as alt, open(files_dir + 'mode.txt', 'r+') as mode:

            # Get all vehicle attributes (state)

            #print("\nGet all vehicle attribute values:")
            #print(" Autopilot Firmware version: %s" % vehicle.version)
            #print("   Major version number: %s" % vehicle.version.major)
            #print("   Minor version number: %s" % vehicle.version.minor)
            #print("   Patch version number: %s" % vehicle.version.patch)
            #print("   Release type: %s" % vehicle.version.release_type())
            #print("   Release version: %s" % vehicle.version.release_version())
            #print("   Stable release?: %s" % vehicle.version.is_stable())
            #print(" Autopilot capabilities")
            #print("   Supports MISSION_FLOAT message type: %s" % vehicle.capabilities.mission_float)
            #print("   Supports PARAM_FLOAT message type: %s" % vehicle.capabilities.param_float)
            #print("   Supports MISSION_INT message type: %s" % vehicle.capabilities.mission_int)
            #print("   Supports COMMAND_INT message type: %s" % vehicle.capabilities.command_int)
            #print("   Supports PARAM_UNION message type: %s" % vehicle.capabilities.param_union)
            #print("   Supports ftp for file transfers: %s" % vehicle.capabilities.ftp)
            #print("   Supports commanding attitude offboard: %s" % vehicle.capabilities.set_attitude_target)
            #print("   Supports commanding position and velocity targets in local NED frame: %s" % vehicle.capabilities.set_attitude_target_local_ned)
            #print("   Supports set position + velocity targets in global scaled integers: %s" % vehicle.capabilities.set_altitude_target_global_int)
            #print("   Supports terrain protocol / data handling: %s" % vehicle.capabilities.terrain)
            #print("   Supports direct actuator control: %s" % vehicle.capabilities.set_actuator_target)
            #print("   Supports the flight termination command: %s" % vehicle.capabilities.flight_termination)
            #print("   Supports mission_float message type: %s" % vehicle.capabilities.mission_float)
            #print("   Supports onboard compass calibration: %s" % vehicle.capabilities.compass_calibration)
            #print(" Global Location: %s" % vehicle.location.global_frame)
            #print(" Global Location (relative altitude): %s" % vehicle.location.global_relative_frame)
            alt.write(str(vehicle.location.global_relative_frame.alt))
            #print(" Local Location: %s" % vehicle.location.local_frame)
            #print(vehicle.attitude)
            #print(" Velocity: %s" % vehicle.velocity)
            #sats = vehicle.gps_0.satellites_visible
            s.write(str(vehicle.gps_0.satellites_visible))
            #print(" Gimbal status: %s" % vehicle.gimbal)
            #volt, current = (vehicle.battery.voltage, vehicle.battery.current)
            v.write(str(vehicle.battery.voltage))
            c.write(str(vehicle.battery.current))
            #print(" EKF OK?: %s" % vehicle.ekf_ok)
            #print(" Last Heartbeat: %s" % vehicle.last_heartbeat)
            #print(" Rangefinder: %s" % vehicle.rangefinder)
            #print(" Rangefinder distance: %s" % vehicle.rangefinder.distance)
            #print(" Rangefinder voltage: %s" % vehicle.rangefinder.voltage)
            #heading = vehicle.heading
            h.write(str(vehicle.heading))
            #print(" Is Armable?: %s" % vehicle.is_armable)
            #print(" System status: %s" % vehicle.system_status.state)
            #gspeed = "{:.2f}".format(vehicle.groundspeed)
            gs.write(str("{:.4f}".format(vehicle.groundspeed)))
            #print(" Airspeed: %s" % vehicle.airspeed)    # settable
            #print(" Mode: %s" % vehicle.mode.name)    # settable
            mode.write(str(vehicle.mode.name)[:4])
            if vehicle.armed == 0:
                arming = "Disarm"
            if vehicle.armed == 1:
                arming = "Armed!"
            arm.write(arming)
            lat.write(str("{:.4f}".format(vehicle.location.global_frame.lat)))
            lon.write(str("{:.4f}".format(vehicle.location.global_frame.lon)))
            #print(vehicle.location.global_frame.lat, vehicle.location.global_frame.lon)
            #print(sats, volt, current, heading)
            sleep(0.2)

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
                    #print(pwmCalc(chans[0]), pwmCalc(chans[1]), pwmCalc(chans[2]), pwmCalc(chans[3]), pwmCalc(chans[4]), pwmCalc(chans[5]), pwmCalc(chans[6]), pwmCalc(chans[7]))
                    rcOverrides(pwmCalc(chans[0]), pwmCalc(chans[1]), pwmCalc(chans[2]), pwmCalc(chans[3]), pwmCalc(chans[4]), pwmCalc(chans[5]), pwmCalc(chans[6]), pwmCalc(chans[7]))
                    sleep(0.01)
            except TimeoutError:
                #print("STOP!")
                rcOverrides(1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500)
                pass
    return bytes(chans)

if __name__ == "__main__":
    vehicleState()
    #openSerial()
