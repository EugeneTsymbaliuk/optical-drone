
# Installation on Ground Station
<img width="786" height="571" alt="Screenshot 2025-11-17 115812" src="https://github.com/user-attachments/assets/726fd13e-9e3a-4c4a-b0fb-5a5be12e147a" />


Ground Station was tested on RP3, RP4 & RP5.
Install latest OS on RPi.
<img width="721" height="394" alt="6" src="https://github.com/user-attachments/assets/ae1c838f-f70b-4a69-903e-4e51564808c7" />

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
<img width="763" height="463" alt="5" src="https://github.com/user-attachments/assets/f59c7df2-0ebd-4449-b569-0db63adfcdef" />

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
sudo nmtui
```
Choose eth0 and add 192.168.10.2/24

7. Open crontab and choose 1
```
crontab -e
```
<img width="660" height="208" alt="4" src="https://github.com/user-attachments/assets/e067e245-adc4-44bf-8623-d2339ef849f0" />

type 1 and add next at the file end
```
@reboot sleep 20; /usr/bin/python3 ~/optical-drone/main_gnd.py &
```
<img width="760" height="583" alt="3" src="https://github.com/user-attachments/assets/4e9bb30d-c7be-4fea-9de6-7a2b10e0280b" />

8. Reboot OS
```
sudo reboot
```
# Installation on Air (Quadrocopter)

![406905698-782968ab-a32a-4c4f-a173-6059ffc1c72f](https://github.com/user-attachments/assets/9a05a59d-1232-4fbc-ad0a-aab2f2a22201)

Install latest OS on RPi.
<img width="721" height="394" alt="6 – копія" src="https://github.com/user-attachments/assets/9a29b8a2-f65a-46a1-a76a-74fcce9f113e" />


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
<img width="923" height="417" alt="2" src="https://github.com/user-attachments/assets/e5b6606a-1f56-4d69-b926-8c806c9b90ef" />

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
12. Open crontab and choose 1
```
crontab -e
```
<img width="660" height="208" alt="4" src="https://github.com/user-attachments/assets/78e2b3b3-a39c-489e-ad92-3af2caa0625f" />

```
@reboot sleep 15; /usr/bin/python3 ~/optical-drone/httpserver.py &
@reboot sleep 20; /usr/bin/python3 ~/optical-drone/main_air.py &
```
<img width="587" height="502" alt="Air_Crontab" src="https://github.com/user-attachments/assets/75f6c61e-ba44-4f0d-bcd2-10d4f69213c6" />

13. Add static IP address
```
sudo nmtui
```
Choose eth0 and add 192.168.10.1/24
14. Reboot OS
```
sudo reboot
```
# Installation on Ground Drone or Quadrocopter (Ardupilot)
<img width="1672" height="2418" alt="449161784-402f1190-5ed0-4b07-8406-937da907502e" src="https://github.com/user-attachments/assets/40e37900-b431-4b04-8f62-87aaad960694" />


Install latest OS on RPi.
<img width="721" height="394" alt="6 – копія" src="https://github.com/user-attachments/assets/30c0e077-8c4a-4cdc-bb6b-6454a9969292" />


Connect to Raspberry Pi, open Terminal and type all commands:

1. Delete EXTERNALLY-MANAGED
```
sudo rm /usr/lib/python3.13/EXTERNALLY-MANAGED
```
2.Download git repository
```
git clone https://github.com/EugeneTsymbaliuk/optical-drone.git
```
3. Go to directory
```
cd ~/optical-drone/
```
4. Run file
```
bash installer_gnd_drone.sh
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
<img width="923" height="417" alt="2" src="https://github.com/user-attachments/assets/2af5f1c6-f252-4c09-b245-2bc9c4e7b6d2" />

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
13. Open crontab and choose 1
```
crontab -e
```

<img width="660" height="208" alt="4" src="https://github.com/user-attachments/assets/92f1158f-c429-4902-a216-0a60983f7810" />

```
@reboot sleep 15; /usr/bin/python3 ~/optical-drone/httpserver.py &
@reboot sleep 20; /usr/bin/python3 ~/optical-drone/main_gnd_drone.py &
```
<img width="611" height="521" alt="Gnd_Drone_crontab" src="https://github.com/user-attachments/assets/41a9f187-23d7-4c39-8ed0-0eb03620ec90" />

14. Add static IP address
```
sudo nmtui
```
Choose eth0 and add 192.168.10.1/24

15. To work dronekit in python from 3.13 you need to
```
nano +2689 ~/.local/lib/python3.13/site-packages/dronekit/__init__.py
change collections.MutableMapping on collections.abc.MuttableMapping
```
<img width="673" height="205" alt="12d8f6e7-b302-4607-817f-719d94ed8989" src="https://github.com/user-attachments/assets/e67765cb-1f38-4dc1-ad12-153a02a43402" />

16. Reboot OS
```
sudo reboot
```
17. Enable Mavlink on UART in Mission Planner

<img width="581" height="549" alt="Capture" src="https://github.com/user-attachments/assets/b70c132b-7cc5-492d-812b-ec54bfdb6248" />

18. Config channels 1&2(right stick of RC) to operate your RC car
![5274098532891692447](https://github.com/user-attachments/assets/03c5baca-1bd8-4358-95c6-dae095e008f1)

# General Info
1. To get video from drone type next in web-browser
```
192.168.10.1:8001
```
2. Check Cameras
```
v4l2-ctl --list-devices

```
3. Get RTSP traffic
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
