#!/bin/sh


lxterminal -e gpio-watch -s /etc/gpio-scripts -e rising 4 15 26 12 23 25 24 20


# get rid of the cursor so we don't see it when videos are running
setterm -cursor on
#setterm -cursor off



# set here the path to the directory containing your videos
#VIDEOPATH="/media/pi/CTCSER/" 

VIDEOPATH="/media/pi/CTCSER"

# you can normally leave this alone
SERVICE="omxplayer"



	# now for our infinite loop with hdmi!
	while true; do
		if ps ax | grep -v grep | grep $SERVICE > /dev/null
		then
		sleep 1;
	else
		for entry in $VIDEOPATH/*
		do
			clear

			# -r for stretched over the entire screen
			xterm -fullscreen -fg black -bg black -e omxplayer -o hdmi $entry > /dev/null
		done
	fi
	done
