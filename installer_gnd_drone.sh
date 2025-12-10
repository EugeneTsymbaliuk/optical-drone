#!/bin/bash

sudo apt update
sudo apt -y upgrade

pip3 install future
pip3 install dronekit

cd ~/
wget https://github.com/bluenviron/mediamtx/releases/download/v1.11.1/mediamtx_v1.11.1_linux_armv6.tar.gz
tar -xvzf mediamtx_v1.11.1_linux_armv6.tar.gz
chmod +x mediamtx

rm ~/optical-drone/*gnd.*
rm ~/optical-drone/*air*

mv ~/optical-drone/index.html
mv ~/optical-drone/
