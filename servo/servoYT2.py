# http://www.youtube.com/watch?v=ddlDgUymbxc
# Mejor:
# http://www.youtube.com/watch?v=N5QmZ92uvUo

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)

p1 = GPIO.PWM(11,50)
p2 = GPIO.PWM(12,50)

p1.start(7.5)

p2.start(7.5)

try:
	while True:
		print "Uno"
		p1.ChangeDutyCycle(7.5)
		time.sleep(1)
		p2.ChangeDutyCycle(7.5)
		time.sleep(1)
		print "Dos"
		p1.ChangeDutyCycle(12.5)
		time.sleep(1)
		p2.ChangeDutyCycle(12.5)
		time.sleep(1)
		print "Tres"
		p1.ChangeDutyCycle(2.5)
		time.sleep(1)
		p2.ChangeDutyCycle(2.5)
		time.sleep(1)

except KeyboardInterrupt:
	GPIO.cleanup()
