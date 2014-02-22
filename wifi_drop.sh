#!/bin/bash
# Original: https://github.com/dirttech/SmartMeter/blob/master/wifi_drop.sh
# Seen in http://raspberrypispot.wordpress.com/2013/07/08/wifi-and-ethernet-dropout-problems-in-raspberry-pi/

while true ; do
if ifconfig wlan0 | grep -q "inet addr:" ; then
sleep 60
   else
echo "Network connection down! Attempting reconnection." | tee -a /home/pi/usr/var/log/varios.log
      ifdown --force wlan0
      sleep 10
      ifup --force wlan0
      sleep 10
    fi
done
