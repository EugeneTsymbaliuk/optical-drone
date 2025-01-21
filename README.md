# Installation
1. Download files(mediamtx_v1.10.0_linux_armv6.tar.gz) for Raspberry Pi from https://github.com/bluenviron/mediamtx/releases or
```
wget https://github.com/bluenviron/mediamtx/releases/download/v1.11.1/mediamtx_v1.11.1_linux_armv6.tar.gz
```
2. Unzip and go to directory
```
tar -xvzf mediamtx_v1.11.1_linux_armv6.tar.gz
```
3. chmod +x mediatx
4. nano +698 mediamtx.yml and add next:
```
paths:
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
5. ./mediatx
6. On VLC type rtsp://192.168.1.187:8554/cam


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
