#!/usr/bin/python
# -*- coding: utf-8 -*-

import smtplib
import email.utils
from email.mime.text import MIMEText

# Create the message
msg = MIMEText('This is the body of the message.')
msg['To'] = email.utils.formataddr(('Me', 'coldturnip@gmail.com'))
msg['Subject'] = 'Hello World!!!'

server = smtplib.SMTP('localhost', 1025)
try:
	server.sendmail('coldturnip@localhost', ['raphanus_lo@asus.com'], msg.as_string())
finally:
	server.quit()

