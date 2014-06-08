# http://www.youtube.com/watch?v=ddlDgUymbxc
# Mejor:
# http://www.youtube.com/watch?v=N5QmZ92uvUo

import RPi.GPIO as GPIO
import time
import sys

from RPIO import PWM









servo = PWM.servo()


GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)

p = GPIO.PWM(11,50)

#p.start(7.5)
p.start(1.0)

print len(sys.argv)

if len(sys.argv) > 1:
	mov = int(sys.argv[1])
else:	
	mov = 0

try:
	print mov
	print "Uno"
	if mov < 0:
		mov = -mov
		sign = -1
	else:
		sign = 1
	for i in range(mov):
		p.ChangeDutyCycle(7.5+sign*i*0.05)
		time.sleep(0.2)

except KeyboardInterrupt:
	GPIO.cleanup()

GPIO.cleanup()
print "Fin"
