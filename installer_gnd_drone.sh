#!/bin/bash

sudo apt update
sudo apt -y upgrade

sudo rm /usr/lib/python3.11/EXTERNALLY-MANAGED

pip3 install future
pip3 install dronekit

touch ~/starter.sh
echo '#!/bin/bash' >> ~/starter.sh
echo  >> ~/starter.sh
echo 'python ~/optical-drone/main_gnd_drone.py' >> ~/starter.sh
chmod 755 ~/starter.sh

echo "call(['/home/`whoami`/mediamtx'])" >> ~/optical-drone/main_gnd_drone.py

# Change window manager (mutter to openbox-lxde)
sudo sed -i "s/mutter/openbox-lxde/g" /etc/xdg/lxsession/LXDE-pi/desktop.conf
cp -rf /etc/xdg/openbox/ ~/.config/

# Autostart
mkdir -p ~/.config/lxsession/LXDE-pi/
cp /etc/xdg/lxsession/LXDE-pi/* ~/.config/lxsession/LXDE-pi/
echo "/home/`whoami`/starter.sh" >> ~/.config/lxsession/LXDE-pi/autostart

# Screensaver
sed -i /xscreensaver/d ~/.config/lxsession/LXDE-pi/autostart
echo 'xset s noblank' >> ~/.config/lxsession/LXDE-pi/autostart
echo 'xset -dpms' >> ~/.config/lxsession/LXDE-pi/autostart
echo 'xset -s off' >> ~/.config/lxsession/LXDE-pi/autostart

rm ~/optical-drone/*gnd.*
rm ~/optical-drone/*air*
