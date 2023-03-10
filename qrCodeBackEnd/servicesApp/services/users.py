from django.http import HttpResponse
from ..constants.utils import *

def registerUser(request):
    jsons = json.loads(request.body)
    username = jsons['username']
    firstname = jsons['firstname']
    lastname = jsons['lastname']
    email = jsons['email']
    password = jsons['password']
    password = passHash(str(password))
    try:
        con = connectDB()
        cursor = con.cursor()
        cursor.execute("INSERT INTO t_user "
                        f"VALUES (DEFAULT, '{username}', '{lastname}', '{firstname}', '{email}', '{password}', NOW());")
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
        except Exception as e:
            resp = str(e)
    return HttpResponse(resp, content_type="application/json")
