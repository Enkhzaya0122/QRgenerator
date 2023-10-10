from django.http import HttpResponse
from ..constants.utils import *
import json
from rest_framework.decorators import api_view


def registerUser(request):
    jsons = json.loads(request.body)
    if len(jsons["password"]) < 4:
        resp = sendResponse(400,'Password must be 4 or more characters',jsons["action"])
        return resp
    email = jsons['email']
    try:
        con = connectDB()
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM t_user WHERE email = '{email}'")
        if cursor.rowcount != 0:
            resp = sendResponse(400,'Email is already registered',jsons["action"])
            return resp
    except Exception as e:
        resp = sendResponse(400,'Error while checking email',jsons["action"])
        return resp
    username = jsons['username']
    firstname = jsons['firstname']
    lastname = jsons['lastname']
    password = jsons['password']
    password = passHash(str(password))
    try:
        con = connectDB()
        # sendMail(email, mailContent['validate_mail_subject'], mailContent['validate_mail_content1'])
        cursor = con.cursor()
        cursor.execute("INSERT INTO t_user "
                        f"VALUES (DEFAULT, '{username}', '{lastname}', '{firstname}', '{email}', '{password}', NOW(),DEFAULT);")
        resp = sendResponse(200,'Success',jsons["action"])
        cursor.close()
        con.commit()
    except Exception as e:
        resp = sendResponse(400,e,jsons["action"])
    finally:
        disconnectDB(con)
    return resp
    # registerUser

def getUsers(request):
    jsons = json.loads(request.body)
    try:
        con = connectDB()
        cursor = con.cursor()
        
        cursor.execute("SELECT username FROM t_user")
        columns = cursor.description
        respRow = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
        resp = sendResponse(200,respRow,jsons["action"])
        cursor.close()
    except Exception as e:
        resp = sendResponse(400,e,jsons["action"])
    finally:
        disconnectDB(con)
    return resp
    # getUsers

def getUserInfo(request):
    jsons = json.loads(request.body)
    usernum = jsons['usernum']
    try:
        con = connectDB()
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM t_user WHERE usernum = {usernum}")
        columns = cursor.description
        respRow = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
        resp = sendResponse(200,respRow,jsons["action"])
        cursor.close()
    except Exception as e:
        resp = sendResponse(400,e,jsons["action"])
    finally:
        disconnectDB(con)
    return resp
    # getUserInfoz

def loginUser(request):
    jsons = json.loads(request.body)
    email = str(jsons['email']).lower()
    password = passHash(str(jsons['password']))
    try:
        con = connectDB()
        cursor = con.cursor()
        cursor.execute(f"SELECT usernum FROM t_user WHERE LOWER(email) = '{email}' AND password = '{password}' ")
        columns = cursor.description
        respRow = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
        resp = sendResponse(200,respRow,jsons["action"])
        cursor.close()
    except Exception as e:
        resp = sendResponse(400,e,jsons["action"])
    finally:
        disconnectDB(con)
    return resp
    # loginUser

def forgetPassword(request):
    jsons = json.loads(request.body)
    email = str(jsons['email'])
    try:
        sendMail(email, mailContent['forgotPassword_mail_subject'], mailContent['forgotPassword_mail_content1'])
    except Exception as e:
        resp = sendResponse(400,e,jsons["action"])
    finally:
        disconnectDB(con)
    return resp

def Test(request):
    jsons = json.loads(request.body)
    try:
        # sendMail("altansuhaltanbayar100@gmail.com", mailContent['validate_mail_subject'], mailContent['validate_mail_content1'])
        resp = True
    except Exception as e:
        resp = sendResponse(400,e,jsons["action"])
    # finally:
    #     print("done")
    return resp
@api_view(['POST','GET'])
def mainFunction(reqeust):
    json = checkreg(reqeust)
    if json == False:
        resp = sendResponse(400,'Json болгоход алдаа гарлаа',json)
        return HttpResponse(resp, content_type="application/json")
    else:
        try:
            if json['action'] == 'Register':
                resp = registerUser(reqeust)
            if json['action'] == 'getUsers':
                resp = getUsers(reqeust)
            if json['action'] == 'getUserInfo':
                resp = getUserInfo(reqeust)
            if json['action'] == 'Login':
                resp = loginUser(reqeust)
            if json['action'] == 'Test':
                resp = Test(reqeust)
        except Exception as e:
            resp = str(e)
    
    return HttpResponse(resp, content_type="application/json")
