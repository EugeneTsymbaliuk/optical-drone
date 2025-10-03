#!/bin/bash

sudo apt update
sudo apt -y upgrade

cd ~/
wget https://github.com/bluenviron/mediamtx/releases/download/v1.11.1/mediamtx_v1.11.1_linux_armv6.tar.gz
tar -xvzf mediamtx_v1.11.1_linux_armv6.tar.gz
chmod +x mediamtx

rm ~/optical-drone/*gnd*
