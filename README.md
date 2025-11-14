
# Installation on Ground Station

Ground Station as tested on RP3, p4 & RP5.
Install latest OS on RPi.

Connect to Raspberry Pi, open Terminal and type all commands:

1. Download git repository
```
git clone https://github.com/EugeneTsymbaliuk/optical-drone.git
```
2. Go to directory
```
cd ~/optical-drone/
```
3. Run file
```
bash installer_gnd.sh
```
4. Enable UART1 on Raspberry pi. Add text in the end of the file /boot/config.txt
```
sudo nano /boot/firmware/config.txt
```
```
enable_uart=1
dtoverlay=disable-bt
dtoverlay=uart0
```
5. Enable Serial Port on Raspberry pi
```
sudo raspi-config
```
-	Select option 3 - Interface Options
-	Select option P6 - Serial Port

(Attention):
At the prompt “Would you like a login shell to be accessible over serial?”, answer 'No'
At the prompt “Would you like the serial port hardware to be enabled?”, answer 'Yes'
Exit raspi-config and reboot the Raspberry Pi for changes to take effect

6. Add static IP address
```
sudo nano /etc/network/interfaces.d/eth0
```
```
allow-hotplug eth0
iface eth0 inet static
address 192.168.10.2/24
``` 
7. Open crontab 
```
crontab -e
```
and add next at the file end
```
@reboot sleep 20; /usr/bin/python3 ~/optical-drone/main_gnd.py &
```
8. Reboot OS
```
sudo reboot
```
# Installation on Air (Quadrocopter)

![406905698-782968ab-a32a-4c4f-a173-6059ffc1c72f](https://github.com/user-attachments/assets/9a05a59d-1232-4fbc-ad0a-aab2f2a22201)

Install latest OS on RPi.

Connect to Raspberry Pi, open Terminal and type all commands:

Download git repository
```
git clone https://github.com/EugeneTsymbaliuk/optical-drone.git
```
2. Go to directory
```
cd ~/optical-drone/
```
3. Run file
```
bash installer_air.sh
```
4. Enable UART1 on Raspberry pi. Add text in the end of the file /boot/config.txt
```
sudo nano /boot/firmware/config.txt
```
```
enable_uart=1
dtoverlay=disable-bt
dtoverlay=uart0
```
5. Enable Serial Port on Raspberry pi
```
sudo raspi-config
```
-	Select option 3 - Interface Options
-	Select option P6 - Serial Port

(Attention):
At the prompt “Would you like a login shell to be accessible over serial?”, answer 'No'
At the prompt “Would you like the serial port hardware to be enabled?”, answer 'Yes'
Exit raspi-config and reboot the Raspberry Pi for changes to take effect

6. Go to directory
```
cd ~/
```
7. Add text in file mediamtx.yml and add text under paths:
```
  cam:
    source: rpiCamera
    rpiCameraWidth: 1296
    rpiCameraHeight: 972
    rpiCameraVFlip: true
    rpiCameraHFlip: true
    rpiCameraBitrate: 1500000
    rpiCameraFPS: 30
  #  For Thermal Camera
  #  cam:
  #    runOnInit: ffmpeg -f v4l2 -i /dev/video0 -tune zero_latency -framerate 25  -f mpegts -omit_video_pes_length 1 udp:192.168.1.155:9000
  #    runOnInitRestart: yes
```
8. Move the server executable and configuration in global folders
```
sudo mv mediamtx /usr/local/bin/
sudo mv mediamtx.yml /usr/local/etc/
```
9. Create a systemd service:
```
sudo tee /etc/systemd/system/mediamtx.service >/dev/null << EOF
[Unit]
Wants=network.target
[Service]
ExecStart=/usr/local/bin/mediamtx /usr/local/etc/mediamtx.yml
[Install]
WantedBy=multi-user.target
EOF
```
10. Enable and start the service:
```
sudo systemctl daemon-reload
sudo systemctl enable mediamtx
sudo systemctl start mediamtx
```
11. Disable Desktop
```
sudo raspi-config
```
- Select option 1 - System Options
- Select option S5 - Boot / Autologin
- Select option B1 - Console
12. Open crontab
```
@reboot sleep 20; /usr/bin/python3 ~/optical-drone/main_air.py &
```
13. Add static IP address
```
sudo nano /etc/network/interfaces.d/eth0
```
```
allow-hotplug eth0
iface eth0 inet static
address 192.168.10.1/24
``` 
14. Open crontab 
```
crontab -e
```
and add next at the file end
```
@reboot sleep 20; /usr/bin/python3 ~/optical-drone/main_air.py &
```
15. Reboot OS
```
sudo reboot
```
# Installation on Ground Drone (Ardupilot)
<img width="1672" height="2418" alt="449161784-402f1190-5ed0-4b07-8406-937da907502e" src="https://github.com/user-attachments/assets/40e37900-b431-4b04-8f62-87aaad960694" />


Install latest OS on RPi.

Connect to Raspberry Pi, open Terminal and type all commands:

1.Download git repository
```
git clone https://github.com/EugeneTsymbaliuk/optical-drone.git
```
2. Go to directory
```
cd ~/optical-drone/
```
3. Run file
```
bash installer_gnd_drone.sh
```
4. Delete EXTERNALLY-MANAGED
```
sudo rm /usr/lib/python3.13/EXTERNALLY-MANAGED
```
5. Enable UART1 on Raspberry pi. Add text in the end of the file /boot/config.txt
```
sudo nano /boot/firmware/config.txt
```
```
enable_uart=1
dtoverlay=disable-bt
dtoverlay=uart0
```
6. Enable Serial Port on Raspberry pi
```
sudo raspi-config
```
-	Select option 3 - Interface Options
-	Select option P6 - Serial Port

(Attention):
At the prompt “Would you like a login shell to be accessible over serial?”, answer 'No'
At the prompt “Would you like the serial port hardware to be enabled?”, answer 'Yes'
Exit raspi-config and reboot the Raspberry Pi for changes to take effect

7. Go to directory
```
cd ~/
```
8. Add text in file mediamtx.yml and add text under paths:
```
nano +699 mediamtx.yml
```
```
  cam:
    source: rpiCamera
    rpiCameraWidth: 1296
    rpiCameraHeight: 972
    rpiCameraVFlip: true
    rpiCameraHFlip: true
    rpiCameraBitrate: 1500000
    rpiCameraFPS: 30
  #  For Thermal Camera
  #  cam:
  #    runOnInit: ffmpeg -f v4l2 -i /dev/video0 -tune zero_latency -framerate 25  -f mpegts -omit_video_pes_length 1 udp:192.168.1.155:9000
  #    runOnInitRestart: yes
```
9. Move the server executable and configuration in global folders
```
sudo mv mediamtx /usr/local/bin/
sudo mv mediamtx.yml /usr/local/etc/
```
10. Create a systemd service:
```
sudo tee /etc/systemd/system/mediamtx.service >/dev/null << EOF
[Unit]
Wants=network.target
[Service]
ExecStart=/usr/local/bin/mediamtx /usr/local/etc/mediamtx.yml
[Install]
WantedBy=multi-user.target
EOF
```
11. Enable and start the service:
```
sudo systemctl daemon-reload
sudo systemctl enable mediamtx
sudo systemctl start mediamtx
```
12. Disable Desktop
```
sudo raspi-config
```
- Select option 1 - System Options
- Select option S5 - Boot / Autologin
- Select option B1 - Console
13. Open crontab
```
crontab -e
```
and add next at the file end
```
@reboot sleep 20; /usr/bin/python3 ~/optical-drone/main_gnd_drone.py &
```
14. Add static IP address
```
sudo nano /etc/network/interfaces.d/eth0
```
```
allow-hotplug eth0
iface eth0 inet static
address 192.168.10.1/24
``` 
15. To work dronekit in python from 3.11 you need to
```
nano +2689 ~/.local/lib/python3.13/site-packages/dronekit/__init__.py
change collections.MutableMapping on collections.abc.MuttableMapping
```
16. Reboot OS
```
sudo reboot
```
17. Enable Mavlink on UART in Mission Planner

<img width="581" height="549" alt="Capture" src="https://github.com/user-attachments/assets/b70c132b-7cc5-492d-812b-ec54bfdb6248" />

# General Info
1. Check Cameras
```
v4l2-ctl --list-devices

```
2. Get RTSP traffic
```
ffplay rtsp://192.168.1.94:8554/cam
```
# Stream udp traffic from Thermal USB Camera
1. Server Side:
```
ffmpeg -f v4l2 -i /dev/video0 -tune zero_latency -framerate 25  -f mpegts -omit_video_pes_length 1 udp:192.168.1.155:9000
```
2. Client Side:
```
ffplay -fflags nobuffer -flags low_delay -probesize 32 -analyzeduration 1 -strict experimental -framedrop -f mpegts -vf setpts=0 udp://127.0.0.1:9000
```
