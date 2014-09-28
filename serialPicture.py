#!/usr/bin/python
# -*- coding: utf-8 -*-

# Inspired in code seen at:
# http://blog.oscarliang.net/connect-raspberry-pi-and-arduino-usb-cable/
# Some modifications by Fernando Tricas

from serial import Serial
from multiprocessing import Process
import cv2, time
import smtplib, mimetypes, time
from email import Encoders
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email.MIMEMultipart import MIMEMultipart

import mailConfig

destaddr = mailConfig.ADDRESS
fromaddr = mailConfig.FROMADD
toaddrs  = mailConfig.TOADDRS
subject  = mailConfig.SUBJECT
smtpsrv  = mailConfig.SMTPSRV
loginId  = mailConfig.LOGINID
loginPw  = mailConfig.LOGINPW


def mail(imgFile, address=""):
    """Send a file by mail"""

    if (address==""):
        toaddrs = destaddr

    mensaje = MIMEMultipart()

    format, enc = mimetypes.guess_type(imgFile)
    main, sub = format.split('/')
    adjunto = MIMEBase(main, sub)
    adjunto.set_payload(open(imgFile,"rb").read())
    Encoders.encode_base64(adjunto)
    adjunto.add_header('Content-Disposition', 'attachment; filename="%s"' % imgFile)
    mensaje.attach(adjunto)


    mensaje['Subject'] = subject
    mensaje['From'] = fromaddr
    mensaje['To'] = destaddr
    mensaje['Cc'] = toaddrs

    server = smtplib.SMTP()
    #server.set_debuglevel(1)
    server.connect(smtpsrv)
    server.ehlo()
    server.starttls()
    server.login(loginId, loginPw)
    server.sendmail(fromaddr, [destaddr]+[toaddrs], mensaje.as_string(0))
    server.quit() 

    print ("Mail sent")


def camera(imgFile, whichCam):
    """Take a picture"""
    cam=cv2.VideoCapture(whichCam)
    cam.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 1280)
    cam.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 960)
    retval, img = cam.read() 
    cv2.imwrite(imgFile, img)
    del(cam)

ser = Serial('/dev/ttyACM0', 9600)


dist=0
distAnt=0
who=""

while 1:
	distAnt = dist
	dist = int(ser.readline().strip().strip())
	#print dist, distAnt
	if abs(distAnt-dist)>10: 
             print "Alert!!"
             print dist, distAnt
             cam=0
             name = "/tmp/"
             name = name + time.strftime("%Y-%m-%d-%H-%M-%S", time.gmtime())
             name = name + '.png'
	     camera(name,cam)
             p = Process(target=mail, args=(name,who))
             p.start()
             print "Sending picture"
