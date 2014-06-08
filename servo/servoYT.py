# http://www.youtube.com/watch?v=ddlDgUymbxc
# Mejor:
# http://www.youtube.com/watch?v=N5QmZ92uvUo

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)

p = GPIO.PWM(11,50)

p.start(7.5)

try:
	while True:
		print "Uno"
		p.ChangeDutyCycle(7.5)
		time.sleep(1)
		print "Dos"
		p.ChangeDutyCycle(12.5)
		time.sleep(1)
		print "Tres"
		p.ChangeDutyCycle(2.5)
		time.sleep(1)

except KeyboardInterrupt:
	GPIO.cleanup()
