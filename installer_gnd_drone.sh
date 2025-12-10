#!/bin/bash

pip3 install future
pip3 install dronekit

mv ~/optical-drone/index.html ~/index.html 
mv ~/optical-drone/dynamic-updates.js ~/dynamic-updates.js
mkdir ~/files/
mv ~/optical-drone/files/* ~/files/
mv ~/optical-drone/files/* ~/files/

cd ~/
wget https://github.com/bluenviron/mediamtx/releases/download/v1.11.1/mediamtx_v1.11.1_linux_armv6.tar.gz
tar -xvzf mediamtx_v1.11.1_linux_armv6.tar.gz
chmod +x mediamtx

rm ~/optical-drone/*gnd.*
rm ~/optical-drone/*air*
