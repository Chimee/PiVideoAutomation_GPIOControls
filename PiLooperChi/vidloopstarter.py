import subprocess
import RPi.GPIO as GPIO
from time import sleep




GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN) #set GPIO Pin 6 as the input pin
GPIO.setup(5, GPIO.IN) #set GPIO Pin 5 as the input pin

input = GPIO.input(6)
input2 = GPIO.input(5)
#print('original pin reading is : '  input)

#GPIO.add_event_detect(6, GPIO.BOTH)
#def my_callback():
 #   GPIO.output(25, GPIO.input(6))
#GPIO.add_event_callback(6, my_callback)


while True: 
	input = GPIO.input(6)
	input2 = GPIO.input(5)
	if (GPIO.input(6) == False):
		subprocess.call(['/home/pi/PiLooperChi/videolooper.sh']) #Call ALSA (MAX AMP) VidLooper Script
		
		break
		
	else: 
	#Call HDMI Audio Vid Looper Script
		subprocess.call(['/home/pi/PiLooperChi/videolooper2.sh'])
	
		break
		
	#elif ( GPIO.input(6) == False & GPIO.input(5) == False):

	#	print('None High')
		
	#elif (GPIO.input(6) == True & GPIO.input(5) == True):
	#	print('Error, Switch Pointing To Both Audio Configurations')
		
	sleep(1)	
		
		

		
		