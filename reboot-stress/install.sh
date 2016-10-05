#!/bin/sh

LOCAL_PATH=$(pwd)

PARA=$1

if [ $# -eq 1 ]; then
    PARA=$1
    if [ $PARA = "-r" ]; then
        sudo rm /usr/bin/reboot-stress
        sudo rm $HOME/.config/autostart/reboot-stress.desktop
        sudo systemctl enable hciuart
        echo "Remove Complete!!"
        sudo reboot
    fi
fi
if [ $# -eq 0 ]; then
    chmod a+x $LOCAL_PATH/reboot-stress
    sudo cp $LOCAL_PATH/reboot-stress /usr/bin/
    sudo cp reboot-stress.desktop $HOME/.config/autostart
    sudo systemctl disable hciuart
    echo "Install Complete!!"
    sudo reboot
fi
