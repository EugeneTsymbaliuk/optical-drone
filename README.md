1. Download files(mediamtx_v1.10.0_linux_armv6.tar.gz) for Raspberry Pi from https://github.com/bluenviron/mediamtx/releases
2. Unzip and go to directory
3. chmod +x mediatx
4. nano +698 mediamtx.yml and add next:
```
paths:
  cam:
    source: rpiCamera
    rpiCameraWidth: 1080
    rpiCameraHeight: 720
    rpiCameraVFlip: true
    rpiCameraHFlip: true
#    rpiCameraBitrate: 1500000
```
5. ./mediatx
6. On VLC type rtsp://192.168.1.187:8554/cam


# General Info
1. Stream udp traffic from Thermal USB Camera
2. Server Side:
```
ffmpeg -f v4l2 -i /dev/video0 -fflags nobuffer -framerate 25 -f mpegts udp:192.168.1.155:9000
```
3. Client Side:
```
ffplay -fflags nobuffer -flags low_delay -probesize 32 -analyzeduration 1 -strict experimental -framedrop -f mpegts -vf setpts=0 udp://127.0.0.1:9000
```
