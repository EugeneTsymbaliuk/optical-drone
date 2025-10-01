
![GND](https://github.com/user-attachments/assets/4c17ddf0-482c-42a7-bd2f-7fd9baa53c82)
![406905698-782968ab-a32a-4c4f-a173-6059ffc1c72f](https://github.com/user-attachments/assets/9a05a59d-1232-4fbc-ad0a-aab2f2a22201)






# Installation on GND

Download Raspberry Pi Imager and inslall OS on Raspberry Pi (Attention): Install legacy Raspbian Bullseye 64-bit https://www.raspberrypi.com/software/

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
sudo nano /boot/config.txt
```
```
enable_uart=1
dtoverlay=disable-bt
dtoverlay=uart0

# Enable PAL on video
sdtv_mode=2
```
5. Increase Swap
```
sudo dphys-swapfile swapoff
sudo nano /etc/dphys-swapfile
```
 Increase SWAP size from 100Mb to 2048Mb
```
sudo dphys-swapfile setup
sudo dphys-swapfile swapon
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

7. Enable Composite Video
```
sudo raspi-config
```
- Select Option 2 - Display Options -> Composite
8. Add static IP address
```
sudo nano /etc/network/interfaces.d/eth0
```
```
allow-hotplug eth0
iface eth0 inet static
address 192.168.10.2/24
``` 
9. Reboot OS
```
sudo reboot
```
# Installation on Air
Download Raspberry Pi Imager and inslall OS on Raspberry Pi (Attention): Install legacy Raspbian Bullseye 32-bit https://www.raspberrypi.com/software/

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
sudo nano /boot/config.txt
```
```
enable_uart=1
dtoverlay=disable-bt
dtoverlay=uart0

# Enable PAL on video
sdtv_mode=2
```
5. Increase Swap 
```
sudo dphys-swapfile swapoff
sudo nano /etc/dphys-swapfile
```
Increase SWAP size from 100Mb to 512M
```
sudo dphys-swapfile setup
sudo dphys-swapfile swapon
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

8. Download files(mediamtx_v1.10.0_linux_armv6.tar.gz) for Raspberry Pi from https://github.com/bluenviron/mediamtx/releases
```
wget https://github.com/bluenviron/mediamtx/releases/download/v1.11.1/mediamtx_v1.11.1_linux_armv6.tar.gz
```
9. Unzip file
```
tar -xvzf mediamtx_v1.11.1_linux_armv6.tar.gz
```
10. Make file executable
```
chmod +x mediamtx
```
11. Add text in file mediamtx.yml and add text under paths:
```
nano +699 mediamtx.yml
```
Under line paths: 
add next text with according space

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
12. Add static IP address
```
sudo nano /etc/network/interfaces.d/eth0
```
```
allow-hotplug eth0
iface eth0 inet static
address 192.168.10.1/24
``` 
13. Reboot OS
```
sudo reboot
```
# Ground Drone on Arupilot
<img width="1672" height="2418" alt="449161784-402f1190-5ed0-4b07-8406-937da907502e" src="https://github.com/user-attachments/assets/f7ad5123-de71-4c74-8c2c-9517da712c21" />
1. Enable Mavlink on UART
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
