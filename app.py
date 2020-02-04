#!/usr/local/bin/python3

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from collections import deque
from os import environ
import smtplib
import fileinput
import re
import time

RECEPIENT = environ.get('RECEPIENT', None)

USERNAME = environ.get('MAIL_USERNAME', None)
PASSWORD = environ.get('MAIL_PASSWORD', None)

MAIL_HOSTNAME = environ.get('MAIL_HOSTNAME', None)
MAIL_PORT = int(environ.get('MAIL_PORT', None))

LINES = int(environ.get('LINES', 10))

if not USERNAME or not PASSWORD or not MAIL_HOSTNAME:
    exit('Incorrect configuration')

if not RECEPIENT:
    RECEPIENT = USERNAME

if MAIL_PORT:
    server = smtplib.SMTP_SSL(MAIL_HOSTNAME, MAIL_PORT)
else:
    server = smtplib.SMTP_SSL(MAIL_HOSTNAME)

server.login(USERNAME, PASSWORD)

pattern = re.compile(r".*Error")
log_lines = deque(maxlen=LINES+1)

def sendmail():
    message = MIMEMultipart()
    message['From'] = USERNAME
    message['To'] = RECEPIENT
    message['Subject'] = "Error report"
    message.attach(MIMEText(''.join(log_lines), 'plain'))
    server.sendmail(USERNAME, RECEPIENT, message.as_string())


for line in fileinput.input():
    log_lines.append(line)
    if bool(pattern.match(line)):
        sendmail()
            
