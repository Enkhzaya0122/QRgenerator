import psycopg2
import hashlib
import smtplib
import json
import datetime
from .constants import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def connectDB():
    con = psycopg2.connect(
    dbname = dbname[0],
    user = user[0],
    host = host[0],
    password = password[0],
    port = port[0],   
    )
    return con
#   connectDB

def disconnectDB(con):
    if(con):
        con.close()
#   disconnectDB

def passHash(password):
    return hashlib.md5(password.encode('utf-8')).hexdigest()
#   passHash

def checkreg(request):
    try:
        jsons = json.loads(request.body)
    except:
        return False
    return jsons
#   checkreg

def sendResponse(resultcode,data, action):
    response = {}
    response['date'] = datetime.datetime.now()
    response['resultCode'] = resultcode
    response['resultMessage'] = resultMessages[resultcode]
    response["data"] = data
    response["size"] = len(data)
    response["action"] = action
    return json.dumps(response, indent=4, sort_keys=True, default=str)
#   sendResponse

def sendMail(receiver_address, mail_subject, mail_content):
    message = MIMEMultipart()
    message['From'] = EMAIL_SENDER
    message['To'] = receiver_address
    message['Subject'] = mail_subject
    message.attach(MIMEText(mail_content, 'plain'))
    session = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    session.login(EMAIL_SENDER, PASS_SENDER)
    text = message.as_string()
    session.sendmail(EMAIL_SENDER, receiver_address, text)
    session.quit()
#   sendMail

