import psycopg2
import hashlib
import json
import datetime
from .constants import *

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


