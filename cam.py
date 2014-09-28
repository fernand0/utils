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

cam.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 1280)
cam.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 960)

#cam.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 640)
#cam.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 480)
#cam.set(cv2.cv.CV_CAP_PROP_FRAME_EXPOSURE, 2)

def get_image():
	# read is the easiest way to get a full image out of a VideoCapture object.  
	retval, im = cam.read() 
	print retval
	return im

print("Disparo")

img=get_image()


cv2.imwrite(imgFile, img)

#cam.set(cv2.cv.CV_CAP_PROP_FRAME_EXPOSURE, 0)

del(cam)
