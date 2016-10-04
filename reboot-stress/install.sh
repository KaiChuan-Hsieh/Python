#!/bin/sh

LOCAL_PATH=$(pwd)

chmod a+x $LOCAL_PATH/reboot-stress
sudo cp $LOCAL_PATH/reboot-stress /usr/bin/
sudo cp reboot-stress.desktop $HOME/.config/autostart
echo "Install Complete!!"
