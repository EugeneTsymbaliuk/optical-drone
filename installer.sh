#!/bin/bash

sudo apt update
sudo apt -y upgrade

touch ~/starter.sh
echo '#!/bin/bash' >> ~/starter.sh
echo  >> ~/starter.sh
echo 'python ~/fly_by_ip_gnd.py' >> ~/starter.sh
echo './mediatx' >> ~/starter.sh
chmod 755 ~/starter.sh

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

# Enable UART1 on Raspberry pi

echo 'enable_uart=1' >> /boot/config.txt
echo 'dtoverlay=disable-bt' >> /boot/config.txt
echo 'dtoverlay=uart0' >> /boot/config.txt
echo '# Enable PAL on video' >> /boot/config.txt
echo 'sdtv_mode=2' >> /boot/config.txt
