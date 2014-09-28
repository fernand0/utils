#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib
import mimetypes
import time
import optparse

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

imgFile  = '/tmp/imagen.png'


parser = optparse.OptionParser()
(options, args) = parser.parse_args()


if len(args) > 1:
	imgFile  = args[0]
	destaddr = args[1]
elif len(args) > 0:
	destaddr = args[0]



print("Enviando ")

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
