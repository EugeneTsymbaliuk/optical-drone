1. Download files(mediamtx_v1.10.0_linux_arm64v8.tar.gz) for Raspberry Pi from https://github.com/bluenviron/mediamtx/releases
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
5. Run ./mediatx
6. On VLC type rtsp://192.168.1.187:8554/cam
