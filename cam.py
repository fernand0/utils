#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import time
import optparse

imgFile  = '/tmp/imagen.png'

parser = optparse.OptionParser()
(options, args) = parser.parse_args()

if len(args) > 0:
	imgFile = args[0]


cam=cv2.VideoCapture(0)

def get_image():
	# read is the easiest way to get a full image out of a VideoCapture object.  
	retval, im = cam.read() 
	return im



#cam.set(3,640)
#cam.set(4,480)

#for i in xrange(40):
#	temp = get_image()

print("Disparo")

img=get_image()

cv2.imwrite(imgFile, img)

del(cam)
