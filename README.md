# Installation

1. Download installation file
```
For GND
wget https://github.com/EugeneTsymbaliuk/optical-drone/raw/refs/heads/main/installer_gnd.sh

For Air
wget https://github.com/EugeneTsymbaliuk/optical-drone/raw/refs/heads/main/installer_air.sh
```
2. Run file
```
For GND:
bash installer_gnd.sh
bash installer_air.sh
For Air:

```
3. Enable UART1 on Raspberry pi. Add text in the end of the file /boot/config.txt
```
sudo nano /boot/config.txt

enable_uart=1
dtoverlay=disable-bt
dtoverlay=uart0

# Enable PAL on video
sdtv_mode=2
```
4. Increase Swap to RAM size from 100Mb to 512Mb (for RP Zero) or to 2048Mb (for RP 4) 
```
sudo dphys-swapfile swapoff
sudo nano /etc/dphys-swapfile
sudo dphys-swapfile setup
sudo dphys-swapfile swapon
```
5. Enable Serial Port on Raspberry pi
```
sudo raspi-config

-	Select option 3 - Interface Options
-	Select option P6 - Serial Port

(Attention):
At the prompt “Would you like a login shell to be accessible over serial?”, answer 'No'
At the prompt “Would you like the serial port hardware to be enabled?”, answer 'Yes'
Exit raspi-config and reboot the Raspberry Pi for changes to take effect
```
6. Enable Composite Video
```
sudo raspi-config

- Select Option 2 - Display Options -> Composite
```
- Next installation only for Air unit.
7. Download files(mediamtx_v1.10.0_linux_armv6.tar.gz) for Raspberry Pi from https://github.com/bluenviron/mediamtx/releases
```
wget https://github.com/bluenviron/mediamtx/releases/download/v1.11.1/mediamtx_v1.11.1_linux_armv6.tar.gz
```
8. Unzip file
```
tar -xvzf mediamtx_v1.11.1_linux_armv6.tar.gz
```
9. Make file executable
```
chmod +x mediamtx
```
10. Add text in file mediamtx.yml and add text under paths:
```
nano +699 mediamtx.yml

  cam:
    source: rpiCamera
    rpiCameraWidth: 1296
    rpiCameraHeight: 972
    rpiCameraVFlip: true
    rpiCameraHFlip: true
#    rpiCameraBitrate: 1500000
#  For Thermal Camera
#  cam:
#    runOnInit: ffmpeg -f v4l2 -i /dev/video0 -tune zero_latency -framerate 25  -f mpegts -omit_video_pes_length 1 udp:192.168.1.155:9000
#    runOnInitRestart: yes

```
11. Run video streaming (only on Air)
```
./mediamtx
```
12. On Ground Station go to Web-browser and type
```
http://192.168.10.1:8889/cam
```

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
